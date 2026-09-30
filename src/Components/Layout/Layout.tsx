import { ReactNode } from 'react';
import styles from './Layout.module.css';
import Footer from '../Footer/Footer';
import { ScrollToTopButton } from '../ScrollToTopButton/ScrollToTopButton';

const ORBS = [styles.orbViolet1, styles.orbAmber1, styles.orbIndigo2, styles.orbAmber2];

export const Layout = ({ children }: { children: ReactNode }) => (
  <>
    <div className={styles.cosmicLayer}>
      {ORBS.map((orb, i) => (
        <div key={i} className={`${styles.cosmicOrb} ${orb}`} />
      ))}
      <div className={styles.orbSubtleMesh} />
    </div>

    <div className={styles.appViewport}>
      <main className={styles.contentConstraint}>{children}</main>
      <Footer />
      <ScrollToTopButton />
    </div>
  </>
);
