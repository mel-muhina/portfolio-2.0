import { ReactNode } from 'react';
import styles from './Layout.module.css';
import Footer from '../Footer/Footer';
import { ScrollToTopButton } from '../ScrollToTopButton/ScrollToTopButton';

export const Layout = ({ children }: { children: ReactNode }) => {
  return (
    <>
      <div className={styles['cosmic-layer']}>
        <div className={`${styles['cosmic-orb']} ${styles['orb-violet-1']}`}></div>
        <div className={`${styles['cosmic-orb']} ${styles['orb-amber-1']}`}></div>
        <div className={`${styles['cosmic-orb']} ${styles['orb-indigo-2']}`}></div>
        <div className={`${styles['cosmic-orb']} ${styles['orb-amber-2']}`}></div>
        <div className={styles['orb-subtle-mesh']}></div>
      </div>

      <div className={styles['app-viewport']}>
        <main className={styles['content-constraint']}>
          {children}
        </main>
        <Footer />
        <ScrollToTopButton />
      </div>
    </>
  );
}
