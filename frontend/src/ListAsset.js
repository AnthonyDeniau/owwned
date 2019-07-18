import React, { Component } from "react";
import { Button,  List, Typography ,Breadcrumb } from 'antd';
import "antd/dist/antd.css";

const owned = [
  {"date":'04-06-2018',"asset":"asset1","owner":"Beatrice Krum"},
  {"date":'09-11-2019',"asset":"asset2","owner":"Killy Kim"},
]
const available=[
  {"location":'Bat B, L1, C101',"asset":"asset3","owner":"Hermino Moreno"},
  {"location":'Bat D, L1, C212',"asset":"asset4","owner":"Larry Sanders"},
  {"location":'Nowhere',"asset":"asset5","owner":"Clodia Cole"}
];

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

class ListsComponent extends React.Component{
    render(){
        return(
            <List
                header={<h3>{this.props.header}</h3>}
                bordered
                dataSource={this.props.data}
                renderItem={item => (
                    <List.Item>
                        <List.Item.Meta title = {item.asset}
                        description = {item.owner} 
                        />
                        <p></p>
                    <Typography.Text mark>[ITEM]</Typography.Text> {item.asset}
                    </List.Item>
                )}
            />
        );
    }
}

class ListAsset extends React.Component{
    render(){
        return(
            <div>
                <ListsComponent header="Lent" data={owned}/>
                <ListsComponent header="Assets" data={available}/>
            </div>
        );
    }
}

export default ListAsset;