import React from 'react';
import styles from './Header.module.css';

export default function Header() {
  return (
    <header className={styles['glass-header-shell']}>
      <nav className={styles['glass-navbar']}>
        <a className={styles['brand-cluster']} href="#">
          <div className={styles['brand-meta']}>
            <span className={styles['brand-name']}>Mel Muhina</span>
            <span className={styles['brand-sub']}>Full-Stack Software Engineer</span>
          </div>
        </a>
        <div className={styles['nav-links-deck']}>
          <a className={`${styles['nav-pill']} ${styles.active}`} href="#about">About</a>
          <a className={styles['nav-pill']} href="#projects">Projects</a>
          <a className={styles['nav-pill']} href="#timeline">Experience</a>
        </div>
        <a className={styles['nav-cta-btn']} href="mailto:alex@vance.engineering">
          <span>Get in Touch</span>
          <span className="material-symbols-outlined" style={{ fontSize: 18 }}>north_east</span>
        </a>
      </nav>
    </header>
  );
}
