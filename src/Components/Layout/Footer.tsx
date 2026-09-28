// import React from 'react';
// import styles from './Footer.module.css';
//
// export default function Footer() {
//   return (
//     <footer className={styles['glass-footer']}>
//       <div className={`${styles['content-constraint']} ${styles['footer-content']}`}>
//         <div className={styles['footer-columns-grid']}>
//           {/* Col 1 */}
//           <div>
//             <div className={styles['brand-cluster']} style={{ marginBottom: '0.75rem' }}>
//               <span className={styles['brand-name']} style={{ fontSize: '1.2rem' }}>AX // Alex Vance</span>
//               <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', background: 'rgba(255,255,255,0.06)', padding: '2px 6px', borderRadius: '4px', color: 'var(--color-primary)' }}>
//                 v4.2.0-prod
//               </span>
//             </div>
//             <p style={{ fontSize: '0.875rem', color: 'var(--color-text-muted)', lineHeight: 1.6, maxWidth: '340px' }}>
//               Senior Full-Stack Engineer engineering high-concurrency cloud systems, reactive distributed state, and modern interfaces.
//             </p>
//             <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginTop: '1rem' }}>
//               <span className={styles['green-radiant-pulse']}></span>
//               <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: 'var(--color-text-dim)' }}>
//                 All Nodes Operational • Latency 14ms
//               </span>
//             </div>
//           </div>
//
//           {/* Col 2 */}
//           <div>
//             <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: 'var(--color-primary)', letterSpacing: '0.1em', textTransform: 'uppercase' }}>
//               Core Runtime Stack
//             </span>
//             <div className={styles['arsenal-badge-flow']} style={{ marginTop: '0.85rem' }}>
//               <span className={styles['frosted-badge']}>TypeScript</span>
//               <span className={styles['frosted-badge']}>React 19</span>
//               <span className={styles['frosted-badge']}>Next.js App Router</span>
//               <span className={styles['frosted-badge']}>Node.js</span>
//               <span className={styles['frosted-badge']}>Python / FastAPI</span>
//               <span className={styles['frosted-badge']}>AWS Distributed</span>
//               <span className={styles['frosted-badge']}>GraphQL</span>
//               <span className={styles['frosted-badge']}>Docker</span>
//             </div>
//           </div>
//
//           {/* Col 3 */}
//           <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
//             <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: 'var(--color-text-dim)', letterSpacing: '0.1em', textTransform: 'uppercase' }}>
//               Protocols & Social
//             </span>
//             <div style={{ display: 'flex', flexDirection: 'column', gap: '0.4rem', fontSize: '0.875rem' }}>
//               <a className={styles['nav-pill']} href="#" style={{ color: 'var(--color-text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
//                 <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>gh/</span>github
//               </a>
//               <a className={styles['nav-pill']} href="#" style={{ color: 'var(--color-text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
//                 <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>in/</span>linkedin
//               </a>
//               <a className={styles['nav-pill']} href="#" style={{ color: 'var(--color-text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
//                 <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>x/</span>terminal
//               </a>
//               <a className={styles['nav-pill']} href="#" style={{ color: 'var(--color-text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
//                 <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>sub/</span>substack
//               </a>
//             </div>
//           </div>
//         </div>
//
//         <div className={styles['footer-bottom-bar']}>
//           <span>© 2025 Alex Vance. Synthesized with precision. All rights reserved.</span>
//           <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
//             <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8125rem' }}>UTC-0800 • San Francisco, CA</span>
//             <a href="mailto:alex@vance.engineering" style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8125rem', color: 'var(--color-primary)', display: 'inline-flex', alignItems: 'center', gap: '0.35rem' }}>
//               <span className="material-symbols-outlined" style={{ fontSize: '16px' }}>mail</span>
//               alex@vance.engineering
//             </a>
//           </div>
//         </div>
//       </div>
//     </footer>
//   );
// }

import styles from './Footer.module.css';

// Central place for your contact + social details.
const CONTACT = {
  name: 'Mel Muhina',
  tagline:
    'Full-Stack Software Engineer building responsive interfaces, robust APIs, and cloud-native systems.',
  email: 'mel.muhina@gmail.com',
  location: 'London, United Kingdom',
};

const SOCIALS = [
  { label: 'GitHub', prefix: 'gh/', handle: 'mel-muhina', href: 'https://github.com/mel-muhina' },
  { label: 'LinkedIn', prefix: 'in', handle: 'melmuhina', href: 'https://www.linkedin.com/in/melmuhina/' },
  { label: 'Email', prefix: '✉', handle: CONTACT.email, href: `mailto:${CONTACT.email}` },
];

const CORE_STACK = [
  'TypeScript',
  'React',
  'Node.js',
  'Python / FastAPI',
  'Java / Spring Boot',
  'AWS',
];

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className={styles['glass-footer']} id='contact'>
      <div className={`${styles['content-constraint']} ${styles['footer-content']}`}>
        <div className={styles['footer-columns-grid']}>
          {/* Col 1: Brand */}
          <div>
            <div className={styles['brand-cluster']} style={{ marginBottom: '0.75rem' }}>
              <span className={styles['brand-name']} style={{ fontSize: '1.2rem' }}>
                {CONTACT.name}
              </span>
            </div>
            <p className={styles['footer-tagline']}>{CONTACT.tagline}</p>
            <div className={styles['footer-status']}>
              <span className={styles['green-radiant-pulse']}></span>
              <span
                style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: '0.75rem',
                  color: 'var(--color-text-dim)',
                }}
              >
                {CONTACT.location}
              </span>
            </div>
          </div>

          {/* Col 2: Core stack */}
          <div>
            <span className={styles['footer-col-label']}>Core Stack</span>
            <div className={styles['arsenal-badge-flow']} style={{ marginTop: '0.85rem' }}>
              {CORE_STACK.map((tech) => (
                <span key={tech} className={styles['frosted-badge']}>
                  {tech}
                </span>
              ))}
            </div>
          </div>

          {/* Col 3: Socials */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
            <span className={styles['footer-col-label']}>Connect</span>
            <div className={styles['footer-social-list']}>
              {SOCIALS.map((social) => (
                <a
                  key={social.label}
                  className={styles['nav-pill']}
                  href={social.href}
                  target={social.href.startsWith('http') ? '_blank' : undefined}
                  rel={social.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                  style={{
                    color: 'var(--color-text-muted)',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '0.35rem',
                  }}
                >
                  <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--color-primary)' }}>
                    {social.prefix}
                  </span>
                  {social.handle}
                </a>
              ))}
            </div>
          </div>
        </div>
        {/*<span className={styles.bottomBorder}> te</span>*/}

        <div className={styles['footer-bottom-bar']}>
          <span>© {year} {CONTACT.name}. All rights reserved.</span>
        </div>
      </div>
    </footer>
  );
}
