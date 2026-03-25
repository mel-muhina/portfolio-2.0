import styles from './Hero.module.css';

import heroImage from '../../assets/hero/ProfileMini.jpg';

export const Hero = () => {
  return (
    <section className={styles.heroContainer}>
      <div className={styles.heroContent}>
        <h1 className={styles.herotitle}>Hi, I'm Mel!</h1>
        <p className={styles.herodescription}>
          Former teacher turned <b>Software Engineer</b> that specialises in{' '}
          <b>fullstack development</b>. My main tech stack includes <b>Java</b>, <b>Typescript</b>{' '}
          and <b>React</b>, but I love learning new tools and languages.
        </p>
        <a className={styles.herocontactBtn} href="mailto:mel.muhina@gmail.com">
          {' '}
          Contact Me{' '}
        </a>
      </div>
      <img src={heroImage} alt="Mel Muhina" className={styles.heroImg} />
      <div className={styles.topBlur} />
      <div className={styles.bottomBlur} />
    </section>
  );
};
