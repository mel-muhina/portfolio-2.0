import { useState, useEffect } from 'react';
import styles from './ScrollToTopButton.module.css';

export const ScrollToTopButton = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const toggleVisibility = () => {
      if (window.scrollY > 400) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', toggleVisibility, { passive: true });
    return () => window.removeEventListener('scroll', toggleVisibility);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  };

  return (
    <button
      onClick={scrollToTop}
      className={`${styles.scrollToTopBtn} ${isVisible ? styles.visible : ''}`}
      aria-label="Scroll back to top"
    >
      <span className="material-symbols-outlined">arrow_upward</span>
    </button>
  );
};
