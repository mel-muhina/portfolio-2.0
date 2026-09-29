import React from 'react';
import styles from './Timeline.module.css';
import history from '../../Data/history.json';

type HistoryItem = {
  role: string;
  organisation: string;
  startDate: string;
  endDate: string;
  description: string;
  bullets?: string[];
  experiences: string[];
  imageSrc: string;
};

const getHistoryLogo = (fileName: string) => `/history/${fileName}`;

export const Timeline = () => {
  const items = history as HistoryItem[];

  return (
    <section className={styles['portfolio-section']} id="experience">
      <div className={styles['section-head']}>
        <span className={styles['eyebrow-chip']}>
          <span className="material-symbols-outlined" style={{ fontSize: '16px' }}>
            history_edu
          </span>
          EVOLUTION & EXPERIENCE
        </span>
        <h2 className={styles['section-title']}>Career Milestones & Experience</h2>
        <p className={styles['section-desc']}>
          A progression grounded in user centric problem solving, elevated across end to end product engineering and highly performant web applications.
        </p>
      </div>

      <div className={styles['career-timeline-deck']}>
        <div className={styles['vertical-luminescence-spine']}></div>

        {items.map((item, index) => (
          <div key={`${item.organisation}-${index}`} className={styles['timeline-milestone']}>
            <div className={styles['spine-orb-anchor']}></div>
            <div className={styles['glass-milestone-card']}>
              <div className={styles['milestone-brand-line']}>
                <div className={styles['milestone-company-info']}>
                  <img
                    alt={`${item.organisation} Logo`}
                    className={styles['company-logo-avatar']}
                    src={getHistoryLogo(item.imageSrc)}
                  />
                  <div>
                    <span className={styles['milestone-title-text']}>{item.role}</span>
                    <span className={styles['milestone-company-name']}>
                      {' '}@ {item.organisation}
                    </span>
                  </div>
                </div>
                <span className={styles['milestone-tenure-tag']}>
                  {item.startDate} — {item.endDate}
                </span>
              </div>

              {item.bullets && item.bullets.length > 0 ? (
                <ul className={styles['milestone-bullets']}>
                  {item.bullets.map((point, i) => (
                    <li key={i}>{point}</li>
                  ))}
                </ul>
              ) : (
                item.description && (
                  <ul className={styles['milestone-bullets']}>
                    <li>{item.description}</li>
                  </ul>
                )
              )}

              <div
                className={styles['arsenal-badge-flow']}
                style={{
                  marginTop: '1.5rem',
                  paddingTop: '1.25rem',
                  borderTop: '1px solid rgba(255,255,255,0.06)',
                }}
              >
                {item.experiences.map((exp, i) => (
                  <span key={exp} className={styles['frosted-badge']}>
                    {i === 0 && <span className={styles['badge-amber-dot']}></span>}
                    {exp}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}

        <div className={styles['illuminated-pivot-block']}>
          <div className={styles['pivot-header']}>
            <span
              className="material-symbols-outlined"
              style={{ color: 'var(--color-secondary)', fontSize: '22px' }}
            >
              switch_access_shortcut
            </span>
            <span className={styles['pivot-title']}>
              THE PIVOT: FROM TEACHING TO SOFTWARE ENGINEERING
            </span>
          </div>
          <p className={styles['pivot-body']}>
            Before entering software engineering, I spent seven years in teaching, with my background in design. Making the transition was an incredibly enjoyable journey—it was the exact space where my passion for problem-solving, technology, and creativity finally came together. Whether I am architecting full-stack workflows or designing intuitive user interfaces, the core drive remains the same: building systems that are logical, resilient, and beautifully crafted.
          </p>
        </div>
      </div>
    </section>
  );
}
