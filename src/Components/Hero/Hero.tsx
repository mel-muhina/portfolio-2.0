import { useEffect, useRef, useState } from 'react';
import styles from './Hero.module.css';

const TOTAL_FRAMES = 63;
const TOTAL_TRANSITIONS = 9;
const BG_COLOR = '#212455';

function lerpAngle(current, target, factor) {
  let diff = (target - current) % (2 * Math.PI);
  if (diff < -Math.PI) diff += 2 * Math.PI;
  if (diff > Math.PI) diff -= 2 * Math.PI;
  return current + diff * factor;
}

export const Hero = () => {
  const [isMobile, setIsMobile] = useState(false);
  const [ready, setReady] = useState(false);
  const canvasRef = useRef(null);
  const framesRef = useRef([]);
  const transitionsRef = useRef([]);
  const centerImgRef = useRef(null);

  const stateRef = useRef({
    mouseX: -9999,
    mouseY: -9999,
    hasMoved: false,
    isMouseInWindow: true,
    isIdle: false,
    smoothedAngle: 0,

    // Smooth transition state machine:
    // 'CENTER' | 'FROM_CENTER' | 'TRACKING' | 'TO_UP' | 'TO_CENTER'
    mode: 'CENTER',
    currentRotationIndex: 0,
    transitionIndex: 9.0, // 0.0 (UP) to 9.0 (CENTER)

    lastTime: performance.now(),
    idleTimer: null,
  });

  useEffect(() => {
    const checkMobile = () => setIsMobile(window.innerWidth <= 768);
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  useEffect(() => {
    if (isMobile) return;
    const frames = new Array(TOTAL_FRAMES);
    const transitions = new Array(TOTAL_TRANSITIONS);

    const total = 1 + TOTAL_FRAMES + TOTAL_TRANSITIONS;
    let loaded = 0;
    const onOne = () => {
      loaded++;
      if (loaded >= total) setReady(true);
    };

    const centerImg = new Image();
    centerImg.onload = onOne;
    centerImg.onerror = () => {
      centerImg.onload = onOne;
      centerImg.src = '/center.webp';
    };
    centerImg.src = '/frames/center.webp';
    centerImgRef.current = centerImg;

    // Preload 64 circular rotation frames (all 8 compass directions + corners)
    for (let i = 0; i < TOTAL_FRAMES; i++) {
      const img = new Image();
      img.onload = onOne;
      img.onerror = () => {
        img.onload = onOne;
        img.src = `/frames/${i}.webp`;
      };
      img.src = `/frames/frame_${i}.webp`;
      frames[i] = img;
    }
    framesRef.current = frames;

    // Preload 10 transition frames (UP -> CENTER with natural blink)
    for (let i = 0; i < TOTAL_TRANSITIONS; i++) {
      const img = new Image();
      img.onload = onOne;
      img.onerror = () => {
        img.src = '/frames/center.webp';
      };
      img.src = `/frames/transition_${i}.webp`;
      transitions[i] = img;
    }
    transitionsRef.current = transitions;

    return () => {
      framesRef.current = [];
      transitionsRef.current = [];
      centerImgRef.current = null;
      setReady(false);
    };
  }, [isMobile]);

  // Main 60 FPS Canvas Render Loop
  useEffect(() => {
    if (isMobile) return;

    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d', { alpha: false });
    if (!ctx) return;

    let animId;

    const handleResize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      const w = window.innerWidth;
      const h = window.innerHeight;
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };

    handleResize();
    window.addEventListener('resize', handleResize);

    const handleMouseMove = (e) => {
      const state = stateRef.current;
      state.mouseX = e.clientX;
      state.mouseY = e.clientY;
      state.hasMoved = true;
      state.isMouseInWindow = true;
      state.isIdle = false;

      // Reset idle timer (smoothly returns to middle forward eye contact after 3.5s of no motion)
      if (state.idleTimer) clearTimeout(state.idleTimer);
      state.idleTimer = setTimeout(() => {
        state.isIdle = true;
      }, 3500);
    };

    const handleMouseLeave = () => {
      const state = stateRef.current;
      state.isMouseInWindow = false;
    };

    const handleMouseEnter = () => {
      const state = stateRef.current;
      state.isMouseInWindow = true;
      state.isIdle = false;
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        stateRef.current.isMouseInWindow = false;
      }
    };

    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    document.addEventListener('mouseleave', handleMouseLeave);
    document.addEventListener('mouseenter', handleMouseEnter);
    document.addEventListener('visibilitychange', handleVisibilityChange);

    const render = () => {
      const w = window.innerWidth;
      const h = window.innerHeight;
      const state = stateRef.current;

      const now = performance.now();
      const dt = Math.min((now - state.lastTime) / 1000, 0.1);
      state.lastTime = now;

      const nativeW = 1920;
      const nativeH = 1080;
      const scale = Math.max(w / nativeW, h / nativeH);
      const imgW = nativeW * scale;
      const imgH = nativeH * scale;
      const offsetX = (w - imgW) / 2;
      const offsetY = (h - imgH) / 2;

      const faceScreenX = offsetX + imgW * 0.600;
      const faceScreenY = offsetY + imgH * 0.420;

      const enterDeadzoneRadius = Math.min(w, h) * 0.12;
      const exitDeadzoneRadius = Math.min(w, h) * 0.18;

      let dist = 99999;
      let targetAngle = 0;

      if (state.hasMoved && state.mouseX > -1000) {
        const dx = state.mouseX - faceScreenX;
        const dy = state.mouseY - faceScreenY;
        dist = Math.hypot(dx, dy);

        let adjDx = dx;
        let adjDy = dy;

        // Navigation bar vs Top-Right:
        if (state.mouseY < h * 0.35) {
          if (state.mouseX >= w * 0.35 && state.mouseX <= w * 0.65 && state.mouseY < 120) {
            const navProximity = Math.max(0, Math.min(1, (120 - state.mouseY) / 80));
            adjDx = dx * (1.0 - 0.85 * navProximity);
          }
        }

        // Middle bottom of the screen:
        if (state.mouseY > h * 0.60) {
          const bottomWeight = Math.max(0, Math.min(1, (state.mouseY - h * 0.60) / (h * 0.25)));
          const centerSpan = w * 0.55;
          const halfWidth = w * 0.22;
          if (state.mouseX >= centerSpan - halfWidth && state.mouseX <= centerSpan + halfWidth) {
            const centerFactor = Math.max(0, Math.min(1, 1 - Math.abs(state.mouseX - centerSpan) / halfWidth));
            const pullDown = bottomWeight * centerFactor * 0.95;
            adjDx = dx * (1.0 - pullDown);
          }
        }

        // Inverted horizontal projection (-adjDx) aligning character's gaze directly with cursor
        targetAngle = Math.atan2(-adjDx, -adjDy);
        if (targetAngle < 0) targetAngle += 2 * Math.PI;
      }

      // Return to middle if: mouse out of window, idle, or cursor within ~12% radius of face
      // Resume tracking if: cursor moves outside 18% radius while mouse is active
      const wantCenter = !state.isMouseInWindow || state.isIdle || !state.hasMoved || dist <= enterDeadzoneRadius;
      const wantTrack = state.isMouseInWindow && !state.isIdle && state.hasMoved && dist > exitDeadzoneRadius;

      // State machine for pop-free, smooth animations to all corners and back to middle:
      switch (state.mode) {
        case 'CENTER': {
          if (wantTrack) {
            state.mode = 'FROM_CENTER';
            state.transitionIndex = 9.0;
          }
          break;
        }

        case 'FROM_CENTER': {
          if (wantCenter) {
            state.mode = 'TO_CENTER';
          } else {
            // Smoothly lifts gaze from CENTER to UP pose (~0.35s)
            state.transitionIndex -= dt * 26;
            if (state.transitionIndex <= 0) {
              state.transitionIndex = 0;
              state.currentRotationIndex = 0;
              state.smoothedAngle = 0;
              state.mode = 'TRACKING';
            }
          }
          break;
        }

        case 'TRACKING': {
          if (wantCenter) {
            state.mode = 'TO_UP';
            state.transitionIndex = 9.0;
          } else {
            const lerpFactor = 1 - Math.exp(-dt * 13);
            state.smoothedAngle = lerpAngle(state.smoothedAngle, targetAngle, lerpFactor);
            let norm = state.smoothedAngle % (2 * Math.PI);
            if (norm < 0) norm += 2 * Math.PI;
            state.currentRotationIndex = Math.round((norm / (2 * Math.PI)) * TOTAL_FRAMES) % TOTAL_FRAMES;
          }
          break;
        }

        case 'TO_UP': {
          if (wantTrack) {
            state.mode = 'TRACKING';
            state.smoothedAngle = (state.currentRotationIndex / TOTAL_FRAMES) * 2 * Math.PI;
          } else {
            const distCW = (TOTAL_FRAMES - state.currentRotationIndex) % TOTAL_FRAMES;
            const distCCW = state.currentRotationIndex;
            const step = Math.max(1, Math.round(dt * 70));

            if (distCW <= distCCW) {
              state.currentRotationIndex = (state.currentRotationIndex + step) % TOTAL_FRAMES;
              if (state.currentRotationIndex < step && state.currentRotationIndex !== 0) {
                state.currentRotationIndex = 0;
              }
            } else {
              state.currentRotationIndex = (state.currentRotationIndex - step + TOTAL_FRAMES) % TOTAL_FRAMES;
              if (state.currentRotationIndex > TOTAL_FRAMES - step && state.currentRotationIndex !== 0) {
                state.currentRotationIndex = 0;
              }
            }

            if (state.currentRotationIndex === 0) {
              state.mode = 'TO_CENTER';
              state.transitionIndex = 0.0;
            }
          }
          break;
        }

        case 'TO_CENTER': {
          if (wantTrack) {
            state.mode = 'FROM_CENTER';
          } else {
            state.transitionIndex += dt * 18;
            if (state.transitionIndex >= 9.0) {
              state.transitionIndex = 9.0;
              state.mode = 'CENTER';
            }
          }
          break;
        }
      }

      let imgToDraw = null;
      const centerImg = centerImgRef.current;
      const frames = framesRef.current;
      const transitions = transitionsRef.current;

      if (state.mode === 'CENTER') {
        imgToDraw = centerImg || (transitions && transitions[9]);
      } else if (state.mode === 'TRACKING' || state.mode === 'TO_UP') {
        imgToDraw = frames && frames[state.currentRotationIndex];
      } else if (state.mode === 'TO_CENTER' || state.mode === 'FROM_CENTER') {
        const tIdx = Math.min(9, Math.max(0, Math.round(state.transitionIndex)));
        imgToDraw = transitions && transitions[tIdx];
      }

      if (!imgToDraw || !imgToDraw.complete || imgToDraw.naturalWidth === 0) {
        imgToDraw = centerImg;
      }

      ctx.fillStyle = BG_COLOR;
      ctx.fillRect(0, 0, w, h);

      if (imgToDraw && imgToDraw.complete && imgToDraw.naturalWidth > 0) {
        ctx.drawImage(imgToDraw, offsetX, offsetY, imgW, imgH);
      }

      if (imgToDraw && imgToDraw.complete && imgToDraw.naturalWidth > 0) {
        ctx.fillStyle = BG_COLOR;
        ctx.fillRect(0, 0, w, h);
        ctx.drawImage(imgToDraw, offsetX, offsetY, imgW, imgH);
      } else {
        ctx.clearRect(0, 0, w, h);
      }

      animId = requestAnimationFrame(render);
    };

    animId = requestAnimationFrame(render);

    const cleanupState = stateRef.current;
    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseleave', handleMouseLeave);
      document.removeEventListener('mouseenter', handleMouseEnter);
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      cancelAnimationFrame(animId);
      if (cleanupState.idleTimer) clearTimeout(cleanupState.idleTimer);
    };
  }, [isMobile]);

  return (
    <section className={styles.heroSection} id="home" aria-label="mel muhina introduction">

      <img
        src="/backup-img.webp"
        alt="Mel Muhina"
        className={styles.heroCanvas}
        style={{
          zIndex: 2,
          opacity: ready ? 0 : 1,
          transition: 'opacity 0.4s ease',
          pointerEvents: 'none',
        }}
      />

      {isMobile ? (
        <img
          src="/frames/center.webp"
          alt="Mel Muhina"
          className={styles.heroCanvas}
          style={{ objectFit: 'cover', width: '100%', height: '100%', position: 'absolute', top: 0, left: 0, zIndex: 0, backgroundColor: BG_COLOR }}
        />
      ) : (
        <canvas ref={canvasRef} className={styles.heroCanvas} style={{ opacity: ready ? 1 : 0, transition: 'opacity 0.4s ease' }}/>
      )}

      <div className={styles.heroContent}>
        <div className={styles.greetingWrapper}>
          <p className={styles.greeting}>Hi, I&apos;m</p>
        </div>

        <h1 className={styles.heroName}>Mel Muhina</h1>
        <h2 className={styles.heroSubtitle}>Engineering  <span className={styles.heroSubtitleHighlight}>High Quality</span>  User Centric Applications in <span>TypeScript</span>, <span>React</span>, <span>Java</span> and <span>Python</span>.</h2>

        <p className={styles.heroBio}>
          Full Stack Software Engineer who specialises in <strong>React</strong>, <strong>TypeScript</strong>, <strong>Java</strong> and <strong>Python</strong>, dedicated to engineering responsive, highly functional apps where clean code meets intuitive design.
        </p>

        <div className={styles.buttonGroup}>
          <a
            href="#experience"
            className={`${styles.btnPrimary} interactive`}
            data-interactive="true"
          >
            <span>Experience</span>
            <svg
              className={styles.btnIcon}
              width="14"
              height="14"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.4"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
          </a>

          <a
            href="#contact"
            className={`${styles.btnSecondary} interactive`}
            data-interactive="true"
          >
            <span>Let&apos;s Talk</span>
            <svg
              className={styles.btnIcon}
              width="14"
              height="14"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
          </a>
        </div>
      </div>

      <a href="#skills" className={styles.scrollIndicator} aria-label="Scroll to about section">
        <span className={styles.scrollText}>EXPLORE</span>
        <div className={styles.scrollLine}>
          <div className={styles.scrollDot} />
        </div>
      </a>

    </section>
  );
};

export default Hero;
