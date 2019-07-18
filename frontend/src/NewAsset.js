import React, { Component } from "react";
import { Button, List, Layout, Typography, Breadcrumb } from 'antd';
import "antd/dist/antd.css";

const { Header, Footer, Sider, Content } = Layout;

class LineTree extends React.Component{
    render(){
        return(
        <Breadcrumb>
            <Breadcrumb.Item>Org</Breadcrumb.Item>
            <Breadcrumb.Item>
                <a href="">Team 1</a>
            </Breadcrumb.Item>            
        </Breadcrumb>
        );
    }
}

class NewAsset extends React.Component{
    render(){
        return(
            <div>
                Some form
            </div>
        );
    }
}

export default NewAsset;