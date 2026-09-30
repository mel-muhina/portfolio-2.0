import { useMemo } from 'react';
import styles from './Skills.module.css';
import skills from '../../Data/skills.json';

type Category = 'frontend' | 'backend' | 'cloud';
type Skill = { title: string; imageSrc: string; category: Category };

const SKILLS = skills as Skill[];

const getSkillIcon = (fileName: string) => `/skills/${fileName}`;

const COLUMNS: { key: Category; label: string; icon: string }[] = [
  { key: 'frontend', label: 'Frontend Architecture', icon: 'layers' },
  { key: 'backend', label: 'Backend & Data', icon: 'hub' },
  { key: 'cloud', label: 'DevOps & Cloud', icon: 'cloud_done' },
];

const FEATURED_SKILLS = new Set([
  'React',
  'Node.js',
  'Typescript',
  'Javascript',
  'FastAPI',
  'Python',
  'Java',
]);

export const Skills = () => {
  const grouped = useMemo(() => {
    const buckets: Record<Category, Skill[]> = { frontend: [], backend: [], cloud: [] };
    SKILLS.forEach((skill) => {
      buckets[skill.category ?? 'backend'].push(skill);
    });
    return buckets;
  }, []);

  return (
    <div className={styles.arsenalRackShell} id="skills">
      <div className={styles.arsenalHeader}>
        <span className={styles.eyebrowChip}>
          <span className="material-symbols-outlined" style={{ fontSize: '18px' }}>
            memory
          </span>
          ENGINEERING SKILLS
        </span>
        <span className={styles.evaluationStamp}>LATEST EVALUATION: 2026</span>
      </div>

      <div className={styles.arsenalGrid}>
        {COLUMNS.map((col) => (
          <div key={col.key}>
            <div className={styles.arsenalColHeader}>
              <span
                className="material-symbols-outlined"
                style={{ fontSize: '16px', color: 'var(--color-primary)' }}
              >
                {col.icon}
              </span>
              {col.label}
            </div>
            <div className={styles.arsenalBadgeFlow}>
              {grouped[col.key].map((skill, index) => (
                <span key={`${skill.title}-${index}`} className={styles.frostedBadge}>
                  <img
                    className={styles.badgeIcon}
                    src={getSkillIcon(skill.imageSrc)}
                    alt={skill.title}
                  />
                  {skill.title}
                  {FEATURED_SKILLS.has(skill.title) && (
                    <span className={styles.badgeAmberDot} />
                  )}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
