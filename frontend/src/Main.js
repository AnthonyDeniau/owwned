import React, { Component } from "react";
import ApolloClient from "apollo-boost";
import { ApolloProvider } from "react-apollo";
// import { Button, Layout } from "antd";
// import { Route, NavLink, HashRouter } from "react-router-dom";
// import ListAsset from "./ListAsset";
// import NewAsset from "./NewAsset";
import AssetsHomeScreen from "./screens/assets";
import "antd/dist/antd.css";

// const { Header, Footer, Sider, Content } = Layout;

const client = new ApolloClient({
  uri: "http://127.0.0.1:8000/graphql/"
});

class Main extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <AssetsHomeScreen />
      </ApolloProvider>
    );
  }
  //   render() {
  //     return (
  //         <HashRouter>
  //             <div>
  //                 <h1>Owwned</h1>
  //                 <Layout>
  //                     <Header>
  //                         <div className="header">
  //                             <NavLink to="/new">
  //                                 <Button type="primary">New asset</Button>
  //                             </NavLink>
  //                         </div>
  //                     </Header>
  //                     <Content>
  //                         <div className="content">
  //                             <Route exact path="/" component={ListAsset}/>
  //                             <Route path="/new" component={NewAsset}/>
  //                         </div>
  //                     </Content>
  //                 </Layout>
  //             </div>
  //         </HashRouter>
  //     );
  //   }
}

export default Main;
