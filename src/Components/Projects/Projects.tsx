import React, { useMemo, useState } from 'react';
import styles from './Projects.module.css';
import projects from '../../Data/projects.json';

type Category = 'Fullstack' | 'realtime' | 'ai';
type FilterType = 'all' | Category;

type Project = {
  title: string;
  description: string;
  languages: string[];
  demo: string;
  source: string;
  imageSrc: string;
  category: Category;
  keyInfo: string[];
};

const getProjectImage = (fileName: string) => `/projects/${fileName}`;

const FILTERS: { key: FilterType; label: string }[] = [
  { key: 'all', label: 'All Projects' },
  { key: 'Fullstack', label: 'Full-Stack' },
  { key: 'realtime', label: 'Cloud & Real-time' },
  { key: 'ai', label: 'AI & Data' },
];

export const Projects = () => {
  const [activeFilter, setActiveFilter] = useState<FilterType>('all');

  const allProjects = projects as Project[];

  const visibleProjects = useMemo(() => {
    if (activeFilter === 'all') return allProjects;
    return allProjects.filter((p) => p.category === activeFilter);
  }, [activeFilter, allProjects]);

  return (
    <section className={styles['portfolio-section']} id="projects">
      <div className={styles['section-head']}>
        <span className={styles['eyebrow-chip']}>
          <span className="material-symbols-outlined" style={{ fontSize: '16px' }}>
            terminal
          </span>
          FLAGSHIP APPLICATIONS
        </span>
        <h2 className={styles['section-title']}>Featured Projects</h2>
        <p className={styles['section-desc']}>
          End to end applications built for seamless user experiences, lightning fast performance, and rock solid reliability.
        </p>
      </div>

      {/*Not needed for now - decide what to filter by*/}
      {/*<div className={styles['glass-filter-bar']}>*/}
      {/*  {FILTERS.map((filter) => {*/}
      {/*    const count =*/}
      {/*      filter.key === 'all'*/}
      {/*        ? allProjects.length*/}
      {/*        : allProjects.filter((p) => p.category === filter.key).length;*/}
      {/*    return (*/}
      {/*      <button*/}
      {/*        key={filter.key}*/}
      {/*        className={`${styles['filter-chip-btn']} ${*/}
      {/*          activeFilter === filter.key ? styles.active : ''*/}
      {/*        }`}*/}
      {/*        onClick={() => setActiveFilter(filter.key)}*/}
      {/*      >*/}
      {/*        {filter.label} ({count})*/}
      {/*      </button>*/}
      {/*    );*/}
      {/*  })}*/}
      {/*</div>*/}

      <div className={styles['glass-bento-grid']}>
        {visibleProjects.map((project, index) => {
          const isReversed = index % 2 === 1;

          return (
            <div
              key={project.title}
              className={`${styles['glass-card']} ${styles['card-full-span']} ${
                isReversed ? styles['card-reversed'] : ''
              }`}
            >
              <div className={styles['full-span-body']}>
                <div className={styles['proj-meta-header']}>
                  <span
                    className={`${styles['eyebrow-chip']} ${styles['eyebrow-amber']}`}
                  >
                    {(project.header  ?? 'project').toUpperCase()}
                  </span>
                  <h3 className={styles['proj-title']}>{project.title}</h3>
                  <p className={styles['proj-desc']}>{project.description}</p>
                </div>

               {(project.keyInfo&& (
                 <div>
                  <div className={styles.keyInfoContainer}>
                    {project.keyInfo.map((info, idx) => (
                      <span key={idx} className={styles.keyInfoItem}>
                        <span className={styles.keyInfoValue}>{info[0]}</span>
                        <span className={styles.keyInfoLabel}>{info[1]}</span>
                      </span>
                    ))}
                  </div>
                </div>
                ))}

                <div
                  className={styles['arsenal-badge-flow']}
                  style={{ margin: '1.5rem 0' }}
                >
                  {project.languages.map((lang) => (
                    <span key={lang} className={styles['frosted-badge']}>
                      {lang}
                    </span>
                  ))}
                </div>

                <div className={styles['proj-footer-links']}>
                  <a
                    className={styles['btn-action-sm']}
                    href={project.demo}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <span>Watch Demo</span>
                    <span
                      className="material-symbols-outlined"
                      style={{ fontSize: '16px' }}
                    >
                      north_east
                    </span>
                  </a>
                  <a
                    className={styles['link-action-ghost']}
                    href={project.source}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <span
                      className="material-symbols-outlined"
                      style={{ fontSize: '16px' }}
                    >
                      code
                    </span>
                    <span>Inspect Source</span>
                  </a>
                </div>
              </div>

              <div className={styles['full-span-media']}>
              <div className={styles['mac-window-frame']}>

                <div className={styles['mac-topbar']}>
                  <div className={styles['mac-dots']}>
                    <div className={`${styles['mac-dot']} ${styles['mac-dot-red']}`}></div>
                    <div className={`${styles['mac-dot']} ${styles['mac-dot-yellow']}`}></div>
                    <div className={`${styles['mac-dot']} ${styles['mac-dot-green']}`}></div>
                  </div>

                  <span className={styles['mac-url']}>{project.title}</span>

                  <span className={styles['mac-status']}>v1.0</span>
                </div>
                <div className={styles['mac-content']}>
                  <img
                    src={getProjectImage(project.imageSrc)}
                    alt={project.title}
                  />
                </div>
              </div>
            </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
