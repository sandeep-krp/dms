import React from "react";
import Sidebar from "./Sidebar";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";

import Home from "./Home";
import Migrations from "./Migrations";
import Connections from "./Connections";
import Forms from "./Forms";

function Main() {
  return (
    <Router>
      <Sidebar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/migrations" component={Migrations} />
        <Route path="/forms" component={Forms} />
        <Route path="/connections" component={Connections} />
      </Switch>
    </Router>
  );
}

export default Main;
