import React from "react";
import styles from './About.module.css'

import aboutImage from "../../assets/about/aboutImage.png"
import cursor from "../../assets/about/cursorIcon.png"
import design from "../../assets/about/designIcon.png"
import server from "../../assets/about/serverIcon.png"


export const About = () => {
    return (
        <section className={styles.aboutContainer} id="about">
            <h2 className={styles.aboutTitle}>About</h2>
            <div className={styles.aboutContent}>
            <img src={aboutImage} alt="Mel Muhina" className={styles.aboutImg}/>

             <ul className={styles.aboutItems}>
                 <li className={styles.aboutItem}>
                   <img src={cursor} alt="cursor" className={styles.cursorImg}/>
                    <div className={styles.aboutItemText}> 
                        <h3>Frontend Developer</h3>
                        <p>I'm a frontend developer that enjoys designing and building responsive, optimised and beautiful web applications.</p>
                    </div>
                  </li>
                 
                  <li className={styles.aboutItem}>
                   <img src={design} alt="cursor" className={styles.cursorImg}/>
                    <div className={styles.aboutItemText}> 
                        <h3>Eye For Design</h3>
                        <p>With a background in both tech and creative industries, I love designing and creating visually appealing UI.</p>
                    </div>
                  </li>
                   
                  <li className={styles.aboutItem}>
                   <img src={server} alt="cursor" className={styles.cursorImg}/>
                    <div className={styles.aboutItemText}> 
                        <h3>Full Stack Developer</h3>
                        <p>I also enjoy doing some backend development and creating fun APIs to use in my projects. </p>
                    </div>
                  </li>
                </ul>
               
            </div>
        </section>
    )
}