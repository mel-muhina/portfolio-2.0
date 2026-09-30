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

const HISTORY = history as HistoryItem[];

const getHistoryLogo = (fileName: string) => `/history/${fileName}`;

const Icon = ({ name, style }: { name: string; style?: React.CSSProperties }) => (
  <span className="material-symbols-outlined" style={style}>
    {name}
  </span>
);

export const Timeline = () => (
  <section className={styles.portfolioSection} id="experience">
    <div className={styles.sectionHead}>
      <span className={styles.eyebrowChip}>
        <Icon name="history_edu" style={{ fontSize: '16px' }} />
        EVOLUTION & EXPERIENCE
      </span>
      <h2 className={styles.sectionTitle}>Career Milestones & Experience</h2>
      <p className={styles.sectionDesc}>
        A progression grounded in user centric problem solving, elevated across end to end
        product engineering and highly performant web applications.
      </p>
    </div>

    <div className={styles.careerTimelineDeck}>
      <div className={styles.verticalLuminescenceSpine} />

      {HISTORY.map((item, index) => {
        const bullets = item.bullets?.length ? item.bullets : item.description ? [item.description] : [];

        return (
          <div key={`${item.organisation}-${index}`} className={styles.timelineMilestone}>
            <div className={styles.spineOrbAnchor} />
            <div className={styles.glassMilestoneCard}>
              <div className={styles.milestoneBrandLine}>
                <div className={styles.milestoneCompanyInfo}>
                  <img
                    alt={`${item.organisation} Logo`}
                    className={styles.companyLogoAvatar}
                    src={getHistoryLogo(item.imageSrc)}
                  />
                  <div>
                    <span className={styles.milestoneTitleText}>{item.role}</span>
                    <span className={styles.milestoneCompanyName}> @ {item.organisation}</span>
                  </div>
                </div>
                <span className={styles.milestoneTenureTag}>
                  {item.startDate} — {item.endDate}
                </span>
              </div>

              {bullets.length > 0 && (
                <ul className={styles.milestoneBullets}>
                  {bullets.map((point, i) => (
                    <li key={i}>{point}</li>
                  ))}
                </ul>
              )}

              <div className={styles.experienceBadgeFlow}>
                {item.experiences.map((exp, i) => (
                  <span key={exp} className={styles.frostedBadge}>
                    {i === 0 && <span className={styles.badgeAmberDot} />}
                    {exp}
                  </span>
                ))}
              </div>
            </div>
          </div>
        );
      })}

      <div className={styles.illuminatedPivotBlock}>
        <div className={styles.pivotHeader}>
          <Icon
            name="switch_access_shortcut"
            style={{ color: 'var(--color-secondary)', fontSize: '22px' }}
          />
          <span className={styles.pivotTitle}>
            THE PIVOT: FROM TEACHING TO SOFTWARE ENGINEERING
          </span>
        </div>
        <p className={styles.pivotBody}>
          Before entering software engineering, I spent seven years in teaching, with my
          background in design. Making the transition was an incredibly enjoyable journey—it was
          the exact space where my passion for problem-solving, technology, and creativity finally
          came together. Whether I am architecting full-stack workflows or designing intuitive user
          interfaces, the core drive remains the same: building systems that are logical, resilient,
          and beautifully crafted.
        </p>
      </div>
    </div>
  </section>
);
