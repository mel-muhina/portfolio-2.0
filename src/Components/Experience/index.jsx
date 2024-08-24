import { useEffect, useState } from "react";

// import { getImageUrl } from '../../utils.js';
import styles from "./Experience.module.css";
import skills from "../../data/skills.json";
import history from '../../data/history.json';
// import testImg from '../../assets/skills/css.png'


export const Experience = () => {
    const [skilla, setSkillsa] = useState([])
    const [historyItem, setHistoryItem] = useState([])

    const getImageUrl = (fileName) => {
        return `../../skills/${fileName}`; 
    }

    const getImageUrlHistory = (fileName) => {
        return `../../history/${fileName}`; 
    }

    useEffect(() => {
        const urls = skills.map(skill => getImageUrl(skill.imageSrc));
        const mapSkills = skills.map(skill => ({
            ...skill,
            imageSrc: getImageUrl(skill.imageSrc)
        }))

        const mapHistory = history.map(item => ({
            ...item,
            imageSrc: getImageUrlHistory(item.imageSrc)
        }))

        setSkillsa(mapSkills)
        setHistoryItem(mapHistory);

    }, [])


    return (
        <section className={styles.expContainer} id="experience">
            <h2 className={styles.expTitle}>
                Experience
            </h2>
            <div className={styles.expContent}>
                <div className={styles.skills}>{
                   skilla.map((skill, id) => {
                        return (<div key={id} className={styles.skill}>
                        <div className={styles.skillImageContainer}>
                            <img src={skill.imageSrc} alt={skill.title} className={styles.skillimg}/> 
                        </div>
                            <p>{skill.title}</p>
                </div>)
                    
                    })

                 }
                
                
                </div>
                <ul className={styles.history}> {
                    historyItem.map((item, id) => {
                
                        return <li key={id} className={styles.historyItem}>
                            <img  src={item.imageSrc} alt={`${item.organisation} Logo`} />
                            <div className={styles.historyItemDetails}>
                                <h3>{`${item.role}, ${item.organisation}`}</h3>
                                <p>{`${item.startDate}, ${item.endDate}`}</p>
                                <ul>
                                    {item.experiences.map((experience, id) => {
                                    return <li key={id}>{experience}</li>;
                                })}
                                    </ul>
                            </div>
                        </li>
                    })
                        } 
                </ul>
            </div>
        </section>
    )
}