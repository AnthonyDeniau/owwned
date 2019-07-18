import React, { Component } from "react";
import { Button, Layout } from 'antd';
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import ListAsset from "./ListAsset";
import NewAsset from "./NewAsset";


const { Header, Footer, Sider, Content } = Layout;
 
class Main extends Component {
  render() {
    return (
        <HashRouter>
            <div>
                <h1>Owwned</h1>
                <Layout>
                    <Header>
                        <div className="header">
                            <NavLink to="/new">
                                <Button type="primary">New asset</Button>
                            </NavLink>
                        </div>
                    </Header>
                    <Content>
                        <div className="content">
                            <Route exact path="/" component={ListAsset}/>
                            <Route path="/new" component={NewAsset}/>
                        </div>
                    </Content>
                </Layout>
            </div>
        </HashRouter>
    );
  }
}
 
export default Main;