import { useMemo, useState } from 'react';
import styles from './Projects.module.css';
import projects from '../../Data/projects.json';

type Category = 'Fullstack' | 'Frontend';
type FilterType = 'all' | Category;

type Project = {
  title: string;
  description: string;
  languages: string[];
  demo: string;
  liveDemo?: string;
  source: string;
  sourceFrontend?: string;
  sourceBackend?: string;
  imageSrc: string;
  category: Category;
  keyInfo: string[];
  mobileFirst?: boolean;
  mobileImageSrc?: string;
};

const PROJECTS = projects as Project[];
const MAX_VISIBLE = 6;
const ICON_SIZE = { fontSize: '16px' } as const;

const getProjectImage = (fileName: string) => `/projects/${fileName}`;

const FILTERS: { key: FilterType; label: string }[] = [
  { key: 'all', label: 'All Projects' },
  { key: 'Fullstack', label: 'Full-Stack' },
  { key: 'Frontend', label: 'Frontend' },
];

const Icon = ({ name }: { name: string }) => (
  <span className="material-symbols-outlined" style={ICON_SIZE}>
    {name}
  </span>
);

export const Projects = () => {
  const [activeFilter, setActiveFilter] = useState<FilterType>('all');

  const visibleProjects = useMemo(
    () =>
      activeFilter === 'all'
        ? PROJECTS.slice(0, MAX_VISIBLE)
        : PROJECTS.filter((p) => p.category === activeFilter),
    [activeFilter],
  );

  const countFor = (key: FilterType) =>
    key === 'all' ? PROJECTS.length : PROJECTS.filter((p) => p.category === key).length;

  return (
    <section className={styles.portfolioSection} id="projects">
      <div className={styles.sectionHead}>
        <span className={styles.eyebrowChip}>
          <Icon name="terminal" />
          FLAGSHIP APPLICATIONS
        </span>
        <h2 className={styles.sectionTitle}>Featured Projects</h2>
        <p className={styles.sectionDesc}>
          End to end applications built for seamless user experiences, lightning fast
          performance, and rock solid reliability.
        </p>
      </div>

      <div className={styles.glassFilterBar}>
        {FILTERS.map((filter) => (
          <button
            key={filter.key}
            className={`${styles.filterChipBtn} ${
              activeFilter === filter.key ? styles.active : ''
            }`}
            onClick={() => setActiveFilter(filter.key)}
          >
            {filter.label} ({countFor(filter.key)})
          </button>
        ))}
      </div>

      <div className={styles.glassBentoGrid}>
        {visibleProjects.map((project, index) => (
          <article
            key={project.title}
            className={`${styles.glassCard} ${styles.cardFullSpan} ${
              index % 2 === 1 ? styles.cardReversed : ''
            }`}
          >
            <div className={styles.fullSpanBody}>
              <div className={styles.projMetaHeader}>
                <span className={`${styles.eyebrowChip} ${styles.eyebrowAmber}`}>
                  {(project.header ?? 'project').toUpperCase()}
                </span>
                <h3 className={styles.projTitle}>{project.title}</h3>
                <p className={styles.projDesc}>{project.description}</p>
              </div>

              {project.keyInfo && (
                <div className={styles.keyInfoContainer}>
                  {project.keyInfo.map(([value, label]) => (
                    <span key={label} className={styles.keyInfoItem}>
                      <span className={styles.keyInfoValue}>{value}</span>
                      <span className={styles.keyInfoLabel}>{label}</span>
                    </span>
                  ))}
                </div>
              )}

              <div className={styles.arsenalBadgeFlow}>
                {project.languages.map((lang) => (
                  <span key={lang} className={styles.frostedBadge}>
                    {lang}
                  </span>
                ))}
              </div>

              <div className={styles.projFooterLinks}>
                <a
                  className={styles.btnActionSm}
                  href={project.demo}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <span>{project.liveDemo ? 'Live Demo' : 'Watch Demo'}</span>
                  <Icon name="north_east" />
                </a>
                <a
                  className={styles.linkActionGhost}
                  href={project.source}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <Icon name="code" />
                  <span>Inspect Source</span>
                </a>
              </div>
            </div>

            <div className={styles.fullSpanMedia}>
              <div className={styles.macWindowFrame}>
                <div className={styles.macTopbar}>
                  <div className={styles.macDots}>
                    <div className={`${styles.macDot} ${styles.macDotRed}`} />
                    <div className={`${styles.macDot} ${styles.macDotYellow}`} />
                    <div className={`${styles.macDot} ${styles.macDotGreen}`} />
                  </div>
                  <span className={styles.macUrl}>{project.title}</span>
                  <span className={styles.macStatus}>v1.0</span>
                </div>
                <div className={styles.macContent}>
                  <img src={getProjectImage(project.imageSrc)} alt={project.title} />
                </div>
              </div>

              {project.mobileFirst && (
                <div className={styles.phoneOverlay}>
                  <div className={styles.phoneNotch} />
                  <div className={styles.phoneScreen}>
                    <img
                      src={getProjectImage(project.mobileImageSrc ?? project.imageSrc)}
                      alt={`${project.title} mobile view`}
                    />
                  </div>
                </div>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
};
