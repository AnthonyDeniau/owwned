import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import ClassicLayout from "../../layouts/classic";
import AssetDetailScreen from "./detail";
import Assets from "./list";

export default class AssetsHomeScreen extends Component {
  componentDidMount() { }
  render() {
    return (
      <ClassicLayout breadcrumb={[{ text: "Home" }, { text: "Assets" }]}>
        <Router>
          <Route path="/" exact component={Assets} />
          <Route path="/detail" component={AssetDetailScreen} />
        </Router>
      </ClassicLayout>
    );
  }
}
