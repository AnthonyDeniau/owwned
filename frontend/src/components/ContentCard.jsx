import React, { Component } from "react";

export default class ContentCard extends Component {
  render() {
    return (
      <div
        style={{
          background: "#FFFFFF",
          borderRadius: "6px",
          padding: "6px 12px",
          minHeight: "150px",
          maxHeight: this.props.maxHeight,
          overflowY: this.props.maxHeight ? "scroll" : null
        }}
      >
        {this.props.children}
      </div>
    );
  }
}
