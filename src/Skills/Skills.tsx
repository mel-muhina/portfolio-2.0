import React, { useMemo } from 'react';
import styles from './Skills.module.css';
import skills from '../Data/skills.json';

type Category = 'frontend' | 'backend' | 'cloud';
type Skill = { title: string; imageSrc: string; category: Category };

const getSkillIcon = (fileName: string) => `/skills/${fileName}`;

const COLUMNS: { key: Category; label: string; icon: string }[] = [
  { key: 'frontend', label: 'Frontend Architecture', icon: 'layers' },
  { key: 'backend', label: 'Backend & Data', icon: 'hub' },
  { key: 'cloud', label: 'DevOps & Cloud', icon: 'cloud_done' },
];

const featuredSkills = ['React', 'Node.js', 'Typescript', 'Javascript', 'FastAPI', 'Python', 'Java'];

export default function Skills() {
  const grouped = useMemo(() => {
    const buckets: Record<Category, Skill[]> = {
      frontend: [],
      backend: [],
      cloud: [],
    };
    
    (skills as Skill[]).forEach((skill) => {
      const category = skill.category ?? 'backend';
      buckets[category].push(skill);
    });

    return buckets;
  }, []);

  return (
    <div className={styles['arsenal-rack-shell']} id="skills">
      <div className={styles['arsenal-header']}>
        <span className={styles['eyebrow-chip']}>
          <span className="material-symbols-outlined" style={{ fontSize: '18px' }}>
            memory
          </span>
          ENGINEERING SKILLS
        </span>
        <span
          style={{
            fontFamily: 'var(--font-mono)',
            fontSize: '0.75rem',
            color: 'var(--color-text-dim)',
          }}
        >
          LATEST EVALUATION: 2026
        </span>
      </div>

      <div className={styles['arsenal-grid']}>
        {COLUMNS.map((col) => (
          <div key={col.key}>
            <div className={styles['arsenal-col-header']}>
              <span
                className="material-symbols-outlined"
                style={{ fontSize: '16px', color: 'var(--color-primary)' }}
              >
                {col.icon}
              </span>
              {col.label}
            </div>
            <div className={styles['arsenal-badge-flow']}>
              {grouped[col.key].map((skill) => (
                <>

                <span key={skill.title} className={styles['frosted-badge']}>

                  <img
                    src={getSkillIcon(skill.imageSrc)}
                    alt={skill.title}
                    style={{ width: 16, height: 16, objectFit: 'contain' }}
                  />
                  {skill.title}
                  {featuredSkills.includes(skill.title) && <span className={styles['badge-amber-dot']}></span>}
                </span>
                  </>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
