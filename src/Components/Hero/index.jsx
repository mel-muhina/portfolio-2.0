import React from "react";
import styles from './Hero.module.css'

import heroImage from "../../assets/hero/ProfileMini.jpg"


export const Hero = () => {
    return (<section className={styles.heroContainer}>
                    <div className={styles.heroContent}>
                        <h1 className={styles.herotitle}>
                            Hi, I'm Mel!
                        </h1>
                        <p className={styles.herodescription}>Former teacher turned software developer specialising in frontend development. Eager to contribute to projects that combine high quality UI design with fantastic app ideas.  Send me a message if you would like to find out more.</p>
                        <a className={styles.herocontactBtn} href="mailto:mel.muhina@gmail.com"> Contact Me </a>
                     </div>
                     <img src={heroImage} alt="Mel Muhina" className={styles.heroImg}/>
                     <div className={styles.topBlur} />
                     <div className={styles.bottomBlur} />
        </section> )
};
   
