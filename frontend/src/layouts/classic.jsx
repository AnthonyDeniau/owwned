import React, { Component } from "react";
import { Layout, Menu, Breadcrumb } from "antd";
import "./classic.css";

const { Header, Content, Footer } = Layout;

export default class ClassicLayout extends Component {
  render() {
    return (
      <Layout style={{ height: "100%" }}>
        <Header
          style={{
            position: "fixed",
            zIndex: 1,
            width: "100%",
            backgroundColor: "white"
          }}
        >
          <div className="logo">Owwned!</div>
          <Menu mode="horizontal" style={{ lineHeight: "64px" }} />
        </Header>
        <Content
          style={{
            padding: "0 24px",
            marginTop: 64,
            height: "100%"
          }}
        >
          <Breadcrumb style={{ margin: "16px 0" }}>
            {this.props.breadcrumb.map(item => (
              <Breadcrumb.Item>{item.text}</Breadcrumb.Item>
            ))}
          </Breadcrumb>
          <div style={{ minHeight: 380 }}>{this.props.children}</div>
        </Content>
        <Footer style={{ textAlign: "center" }}>RIL 17 ©2018</Footer>
      </Layout>
    );
  }
}
