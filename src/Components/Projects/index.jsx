import { useState, useEffect } from 'react';
import styles from './Projects.module.css'
import projects from '../../Data/projects.json';

export const Projects = () => {
    const [project, setProject] = useState([])

    
    const getImageUrl = (fileName) => {
        return `../../projects/${fileName}`; 
    }

    useEffect(() => {
        const urls = projects.map(skill => getImageUrl(skill.imageSrc));
        const mapProjects = projects.map(project => ({
            ...project,
            imageSrc: getImageUrl(project.imageSrc)
        }))


        setProject(mapProjects)
        console.log("Prohjects", mapProjects)

    }, [])


 return (
    <section className={styles.proContainer}>
    <h2 className={styles.proTitle} id="projects">Recent Projects</h2>

    <div className={styles.proContent}>
        {project.map((projectItem, id) => {

            const codeLanguage = (projectItem) => {
               
                  return projectItem.languages.map((language, index) => (
                    <p key={index}>{language}&nbsp;</p>
                  ));
               
              };
        
            

            return (
                <li key={id} className={styles.projectItem}>
                    <img src={getImageUrl(projectItem.imageSrc)} className={styles.Img} alt={`${projectItem.title} Project Thumbnail`}/>
                    <div className={styles.projectItemDetails}>
                        <h3>{`${projectItem.title}`}</h3>
                        <p>{`${projectItem.description}`}</p>
                    </div>
                    <div className={styles.languages} id={styles.tags}> {codeLanguage(projectItem)} </div>
                    <div>  
                        <p>
                            <a href={projectItem.demo}> <button className={projectItem.demoBtn}>Demo</button> </a> 
                            <a href={projectItem.source}> <button className={projectItem.demoBtn}>Source</button>  </a>
                        </p>
                    </div>  
                      
                   
                </li>
            );
        })}
    </div>
</section>
   ) 
}