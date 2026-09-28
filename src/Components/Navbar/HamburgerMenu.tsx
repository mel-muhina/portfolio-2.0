import styles from './HamburgerMenu.module.css';

interface LinkItem {
  id: string;
  label: string;
}

interface HamburgerMenuProps {
  isOpen: boolean;
  toggle: () => void;
  activeSection: string;
  onNavigate: (e: React.MouseEvent, id: string) => void;
  links: LinkItem[];
}

export const HamburgerMenu = ({ isOpen, toggle, activeSection, onNavigate, links }: HamburgerMenuProps) => {
  return (
    <>
      <button
        className={styles.hamburgerBtn}
        onClick={toggle}
        aria-label="Toggle navigation menu"
      >
        <span className="material-symbols-outlined">
          {isOpen ? 'close' : 'menu'}
        </span>
      </button>

      <div className={`${styles.dropdown} ${isOpen ? styles.show : ''}`}>
        {links.map((link) => (
          <a
            key={link.id}
            href={`#${link.id}`}
            onClick={(e) => onNavigate(e, link.id)}
            className={`${styles.mobileLink} ${activeSection === link.id ? styles.active : ''}`}
          >
            {link.label}
          </a>
        ))}
      </div>
    </>
  );
};
