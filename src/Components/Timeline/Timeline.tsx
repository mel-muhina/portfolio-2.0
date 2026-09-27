// import React from 'react';
// import styles from './Timeline.module.css';
//
// export default function Timeline() {
//   return (
//     <section className={styles['portfolio-section']} id="timeline">
//       <div className={styles['section-head']}>
//         <span className={styles['eyebrow-chip']}>
//           <span className="material-symbols-outlined" style={{ fontSize: '16px' }}>history_edu</span>
//           EVOLUTION & TENURE
//         </span>
//         <h2 className={styles['section-title']}>Career Milestones & Trajectory</h2>
//         <p className={styles['section-desc']}>
//           A progression founded on foundational computational physics, refined across high-velocity startups and mission-critical cloud enterprises.
//         </p>
//       </div>
//
//       <div className={styles['career-timeline-deck']}>
//         <div className={styles['vertical-luminescence-spine']}></div>
//
//         {/* ChronoScale */}
//         <div className={styles['timeline-milestone']}>
//           <div className={styles['spine-orb-anchor']}></div>
//           <div className={styles['glass-milestone-card']}>
//             <div className={styles['milestone-brand-line']}>
//               <div className={styles['milestone-company-info']}>
//                 <img
//                   alt="ChronoScale Logo"
//                   className={styles['company-logo-avatar']}
//                   src="https://lh3.googleusercontent.com/aida/AEtjO1VFOWAVtVzK6c3Zzz3x4QAzfHECp_X-83dnoCV_0Kyfuk8rOhb8ItfNrjd192Md9WVpVdgJGaNARxq39eEdqWvagu9rESHApiAKnGO7nOsWGqBgKD0n_TWlt49E0vws-v0f_9zllF0Mn1Pl_jciiutJZfvdf_sR8kujJSWKyHZKHYfFxpzTLp6KnvfpxKGnbHtiS2FG-BvsHvoSE_aKozgDZIiFeqNq1sfmXXhKwMFRrcd1FzKl4-Ce-fU"
//                 />
//                 <div>
//                   <span className={styles['milestone-title-text']}>Staff / Lead Full-Stack Engineer</span>
//                   <span className={styles['milestone-company-name']}> @ ChronoScale</span>
//                 </div>
//               </div>
//               <span className={styles['milestone-tenure-tag']}>2023 — PRESENT</span>
//             </div>
//             <ul className={styles['milestone-bullets']}>
//               <li>Architected full transition to Next.js App Router and server actions across 8 autonomous engineering squads, slicing hydration times by 40%.</li>
//               <li>Designed an edge-cached multi-tenant state layer over Redis and Cloudflare Workers, handling 4.2 million edge requests per hour with zero downtime.</li>
//               <li>Mentored 12 mid and senior engineers through architectural review processes and advanced TypeScript patterns.</li>
//             </ul>
//             <div className={styles['arsenal-badge-flow']} style={{ marginTop: '1.5rem', paddingTop: '1.25rem', borderTop: '1px solid rgba(255,255,255,0.06)' }}>
//               <span className={styles['frosted-badge']}><span className={styles['badge-amber-dot']}></span>Next.js App Router</span>
//               <span className={styles['frosted-badge']}>TypeScript</span>
//               <span className={styles['frosted-badge']}>Server Actions</span>
//               <span className={styles['frosted-badge']}>Cloudflare Workers</span>
//               <span className={styles['frosted-badge']}>Apache Kafka</span>
//               <span className={styles['frosted-badge']}>Distributed Systems</span>
//               <span className={styles['frosted-badge']}>Team Mentorship</span>
//             </div>
//           </div>
//         </div>
//
//         {/* Apex Data Systems */}
//         <div className={styles['timeline-milestone']}>
//           <div className={styles['spine-orb-anchor']}></div>
//           <div className={styles['glass-milestone-card']}>
//             <div className={styles['milestone-brand-line']}>
//               <div className={styles['milestone-company-info']}>
//                 <img
//                   alt="Apex Data Systems Logo"
//                   className={styles['company-logo-avatar']}
//                   src="https://lh3.googleusercontent.com/aida/AEtjO1U7aRZlF_Zba3l_gUIj5hv3lqopS6ISLBtH1EK6oFo15bLDSWvMMRXfRAolXoNmwb5mZzGv0IWa88e0pEKRL4n8f5P_S2uE_i4jAEPCOed053N1uuhYVlio-CeVvz0EQ88QRV8bS2FqpPY43JmUu7zeF-zAvG05GfPXPGXfq8zJBDO1irE5VQeWoVLJ8ziYzA04VVSbDMEVRJ4C9mqlqxs5EhtCBXc6RkVsEkw_rOUFMtkWrmiBdFcw_rw"
//                 />
//                 <div>
//                   <span className={styles['milestone-title-text']}>Senior Systems & Full-Stack Engineer</span>
//                   <span className={styles['milestone-company-name']}> @ Apex Data Systems</span>
//                 </div>
//               </div>
//               <span className={styles['milestone-tenure-tag']}>2021 — 2023</span>
//             </div>
//             <ul className={styles['milestone-bullets']}>
//               <li>Spearheaded streaming analytics engine transition to ClickHouse and Apache Kafka, reducing query execution costs by 58%.</li>
//               <li>Engineered core React dashboard components handling high-frequency live WebSockets updates without main thread UI jank or memory leaks.</li>
//               <li>Established CI/CD pipeline automated preview environments reducing deploy verification cycle from 45 minutes to 7 minutes.</li>
//             </ul>
//             <div className={styles['arsenal-badge-flow']} style={{ marginTop: '1.5rem', paddingTop: '1.25rem', borderTop: '1px solid rgba(255,255,255,0.06)' }}>
//               <span className={styles['frosted-badge']}><span className={styles['badge-amber-dot']}></span>React</span>
//               <span className={styles['frosted-badge']}>ClickHouse</span>
//               <span className={styles['frosted-badge']}>Apache Kafka</span>
//               <span className={styles['frosted-badge']}>Redis Clusters</span>
//               <span className={styles['frosted-badge']}>WebSockets</span>
//               <span className={styles['frosted-badge']}>CI/CD Pipelines</span>
//               <span className={styles['frosted-badge']}>Performance Tuning</span>
//             </div>
//           </div>
//         </div>
//
//         {/* Veloce Labs */}
//         <div className={styles['timeline-milestone']}>
//           <div className={styles['spine-orb-anchor']}></div>
//           <div className={styles['glass-milestone-card']}>
//             <div className={styles['milestone-brand-line']}>
//               <div className={styles['milestone-company-info']}>
//                 <img
//                   alt="Veloce Labs Logo"
//                   className={styles['company-logo-avatar']}
//                   src="https://lh3.googleusercontent.com/aida/AEtjO1VHO-KcswNIsA_KGPGdcw252BwSwsvxmzxWgRl5eF1snNwbJdOlS4Gws9FpzwHAhLnvpHrDWa4LpReAt_lxt6sihWN3gngl7zTw23Z11uxNV_fVlFHfsQqyw4QJ78XPed-nNYZPk-nAOJBDqvMLLIBfjN0B6ySCUGhAH0J-ZSWWcLpJ31HukybCKsehISC-nLl3va_AS8Mj-xTKD-KqrhAVS9xxEbKoy5EqObaIq70TH3HCBhtK1t8k3QPo"
//                 />
//                 <div>
//                   <span className={styles['milestone-title-text']}>Full-Stack Developer</span>
//                   <span className={styles['milestone-company-name']}> @ Veloce Labs</span>
//                 </div>
//               </div>
//               <span className={styles['milestone-tenure-tag']}>2019 — 2021</span>
//             </div>
//             <ul className={styles['milestone-bullets']}>
//               <li>Developed modular design system with zero runtime CSS overhead, utilized across all commercial client customer portals.</li>
//               <li>Implemented GraphQL microservices in Node.js and Go to aggregate 14 fragmented legacy REST APIs into a unified typed schema.</li>
//             </ul>
//             <div className={styles['arsenal-badge-flow']} style={{ marginTop: '1.5rem', paddingTop: '1.25rem', borderTop: '1px solid rgba(255,255,255,0.06)' }}>
//               <span className={styles['frosted-badge']}><span className={styles['badge-amber-dot']}></span>Node.js</span>
//               <span className={styles['frosted-badge']}>Go / Gin</span>
//               <span className={styles['frosted-badge']}>GraphQL APIs</span>
//               <span className={styles['frosted-badge']}>PostgreSQL</span>
//               <span className={styles['frosted-badge']}>Microservices</span>
//               <span className={styles['frosted-badge']}>Zero-Runtime CSS</span>
//             </div>
//           </div>
//         </div>
//
//         {/* Illuminated The Pivot Callout */}
//         <div className={styles['illuminated-pivot-block']}>
//           <div className={styles['pivot-header']}>
//             <span className="material-symbols-outlined" style={{ color: 'var(--color-secondary)', fontSize: '22px' }}>switch_access_shortcut</span>
//             <span className={styles['pivot-title']}>THE PIVOT: FROM APPLIED PHYSICS TO DISTRIBUTED WEB PLATFORMS</span>
//           </div>
//           <p className={styles['pivot-body']}>
//             Before entering commercial software, I analyzed boundary-layer fluid dynamics and numerical simulations in aerospace labs. The transition to distributed web engineering felt natural: whether balancing mass-conservation equations or engineering backpressure across streaming event queues, solving for throughput, race conditions, and graceful degradation relies on the exact same underlying mental models.
//           </p>
//         </div>
//       </div>
//     </section>
//   );
// }
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

export default function Timeline() {
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

        {/* Illuminated Pivot Callout (static) */}
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
