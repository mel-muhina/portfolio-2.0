import styles from './About.module.css';
import aboutImage from '../../assets/about/aboutImage.png';
import cursor from '../../assets/about/cursorIcon.png';
import design from '../../assets/about/designIcon.png';
import server from '../../assets/about/serverIcon.png';

export const About = () => {
  return (
    <>
      <section className={styles.aboutContainer} id="about">
        <h2 className={styles.aboutTitle}>About</h2>
        <div className={styles.aboutInnerContainer}>
          <div className={styles.aboutContent}>
            <div className={styles.aboutPicTitle}>
              <img src={aboutImage} alt="Mel Muhina" className={styles.aboutImg} />
            </div>

            <ul className={styles.aboutItems}>
              <li className={styles.aboutItem}>
                <img src={cursor} alt="cursor" className={styles.cursorImg} />
                <div className={styles.aboutItemText}>
                  <h3>Fullstack Developer</h3>
                  <p>
                    I'm a fullstack developer with a keen eye for detail that enjoys developing
                    responsive, high quality software and applications that are optimised for a
                    smooth user experience.{' '}
                  </p>
                </div>
              </li>

              <li className={styles.aboutItem}>
                <img src={design} alt="cursor" className={styles.cursorImg} />
                <div className={styles.aboutItemText}>
                  <h3>Architecting Solutions</h3>
                  <p>
                    I excel at taking an idea from concept to deployment. I enjoy architecting the
                    entire system, ensuring the frontend and backend work together seamlessly for
                    the end user.
                  </p>
                </div>
              </li>

              <li className={styles.aboutItem}>
                <img src={server} alt="cursor" className={styles.cursorImg} />
                <div className={styles.aboutItemText}>
                  <h3>User-Centric Development</h3>
                  <p>
                    Beyond just writing code, I focus on the "why", creating intuitive and
                    accessible user experiences. I believe the best applications are not just
                    functional, but are genuinely easy and enjoyable to use.
                  </p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </section>
    </>
  );
};
