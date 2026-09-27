import React, { useState, useEffect } from 'react';
import styles from './Navbar.module.css';

export const Navbar = () => {
  const [activeSection, setActiveSection] = useState('work');

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const windowHeight = window.innerHeight;

      if (scrollY < windowHeight * 0.7) {
        setActiveSection('home');
      } else {
        const aboutEl = document.getElementById('about');
        const projectsEl = document.getElementById('projects');
        const contactEl = document.getElementById('contact');

        const positions = [
          { id: 'projects', top: projectsEl?.getBoundingClientRect().top ?? 9999 },
          { id: 'about', top: aboutEl?.getBoundingClientRect().top ?? 9999 },
          { id: 'contact', top: contactEl?.getBoundingClientRect().top ?? 9999 },
        ];

        const inView = positions.filter((p) => p.top <= windowHeight * 0.4);
        if (inView.length > 0) {
          const closest = inView[inView.length - 1];
          setActiveSection(closest.id);
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (e, id) => {
    e.preventDefault();
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className={styles.header}>
      <nav className={styles.navPill} aria-label="Primary navigation">
        <div className={styles.nameContainer}>
          <a
            href="/home"
            onClick={(e) => scrollToSection(e, 'home')}
            className={`${styles.navLink} ${activeSection === 'home' ? styles.active : ''}`}
            data-interactive="true"
          >
          <span className={styles['brand-name']}>MEL MUHINA</span>
          </a>
        </div>
        <a
          href="/skills"
          onClick={(e) => scrollToSection(e, 'skills')}
          className={`${styles.navLink} ${activeSection === 'skills' ? styles.active : ''}`}
          data-interactive="true"
        >
          <span className={styles.linkText}>Skills</span>
        </a>

        <span className={styles.divider} aria-hidden="true" />


        <a
          href="/projects"
          onClick={(e) => scrollToSection(e, 'projects')}
          className={`${styles.navLink} ${activeSection === 'projects' ? styles.active : ''}`}
          data-interactive="true"
        >
          <span className={styles.linkText}>Projects</span>
        </a>

        <span className={styles.divider} aria-hidden="true" />

        <a
          href="/experience"
          onClick={(e) => scrollToSection(e, 'experience')}
          className={`${styles.navLink} ${activeSection === 'experience' ? styles.active : ''}`}
          data-interactive="true"
        >
          <span className={styles.linkText}>Experience</span>
        </a>

        <span className={styles.divider} aria-hidden="true" />


        <a
          href="/contact"
          onClick={(e) => scrollToSection(e, 'contact')}
          className={`${styles.navLink} ${activeSection === 'contact' ? styles.active : ''}`}
          data-interactive="true"
        >
          <span className={styles.linkText}>Contact</span>
        </a>
      </nav>
    </header>
  );
};
