import React, { useState } from "react";
import {
  RiMenuLine,
  RiLayoutGridFill,
  RiChat4Fill,
  RiTeamFill,
} from "react-icons/ri";
import "./Sidebar.css";
import { Link } from "react-router-dom";

function Sidebar() {
  const sidebarCollapsed = localStorage.getItem("sidebar-collapsed");
  const [isExpanded, setIsExpanded] = useState(sidebarCollapsed ? false : true);

  const handleToggler = () => {
    if (isExpanded) {
      setIsExpanded(false);
      localStorage.setItem("sidebar-collapsed", true);
      return;
    }
    setIsExpanded(true);
    localStorage.removeItem("sidebar-collapsed");
  };

  const handleSidebarItemClick = () => {
    if (isExpanded) {
      setIsExpanded(false);
      localStorage.setItem("sidebar-collapsed", true);
      return;
    }
  };

  return (
    <div className={isExpanded ? "Sidebar" : "Sidebar collapsed"}>
      <div className="sidebar-header">
        <RiMenuLine className="sidebar-icon" onClick={handleToggler} />
        <h1 className="sidebar-logo">Menu</h1>
      </div>
      <div className="sidebar-items">
        <Link to="/" className="sidebar-link">
          <div className="item" onClick={handleSidebarItemClick}>
            <RiLayoutGridFill className="sidebar-icon" />
            <span className="sidebar-text">Home</span>
          </div>
        </Link>
        <Link to="/migrations" className="sidebar-link">
          <div className="item" onClick={handleSidebarItemClick}>
            <RiChat4Fill className="sidebar-icon" />
            <span className="sidebar-text">Migrations</span>
          </div>
        </Link>
        <Link to="/connections" className="sidebar-link">
          <div className="item" onClick={handleSidebarItemClick}>
            <RiTeamFill className="sidebar-icon" />
            <span className="sidebar-text">Connections</span>
          </div>
        </Link>
      </div>
    </div>
  );
}

export default Sidebar;
