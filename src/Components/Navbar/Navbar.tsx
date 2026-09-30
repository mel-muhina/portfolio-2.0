import React, { useState, useEffect } from 'react';
import styles from './Navbar.module.css';
import { HamburgerMenu } from './HamburgerMenu.tsx';

const NAV_LINKS = [
  { id: 'skills', label: 'Skills' },
  { id: 'projects', label: 'Projects' },
  { id: 'experience', label: 'Experience' },
  { id: 'contact', label: 'Contact' }
];

export const Navbar = () => {
  const [activeSection, setActiveSection] = useState('home');
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 10) {
        return setActiveSection('contact');
      }
      const sections = ['contact', 'experience', 'projects', 'skills', 'home'];

      const current = sections.find(id => {
        const el = document.getElementById(id);
        return el && el.getBoundingClientRect().top <= window.innerHeight * 0.3;
      });
      if (current) setActiveSection(current);
    };
    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (e, id) => {
    e.preventDefault();
    setIsMenuOpen(false);
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className={styles.header}>
      <nav className={`${styles.navPill} ${isMenuOpen ? styles.menuOpen : ''}`} aria-label="Primary navigation">
        <div className={styles.topBar}>
          <a
            href="/home"
            onClick={(e) => scrollToSection(e, 'home')}
            className={`${styles.brandLink} ${activeSection === 'home' ? styles.activeBrand : ''}`}
          >
            <span className={styles['brand-name']}>MEL MUHINA</span>
          </a>
          <HamburgerMenu
            isOpen={isMenuOpen}
            toggle={() => setIsMenuOpen(!isMenuOpen)}
            activeSection={activeSection}
            onNavigate={scrollToSection}
            links={NAV_LINKS}
          />
        </div>

        <div className={styles.desktopLinks}>
          {NAV_LINKS.map((link, index) => (
            <React.Fragment key={link.id}>
              <a
                href={`#${link.id}`}
                onClick={(e) => scrollToSection(e, link.id)}
                className={`${styles.navLink} ${activeSection === link.id ? styles.active : ''}`}
              >
                <span className={styles.linkText}>{link.label}</span>
              </a>
              {index < NAV_LINKS.length - 1 && (
                <span className={styles.divider} aria-hidden="true" />
              )}
            </React.Fragment>
          ))}
        </div>
      </nav>
    </header>
  );
};
