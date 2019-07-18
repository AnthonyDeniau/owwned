import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Button, Breadcrumb } from 'antd';
import { Layout } from 'antd';
import { List, Typography } from 'antd';
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

const { Header, Footer, Sider, Content } = Layout;

/*class Square extends React.Component {
    render() {
        return (
        <button className="square">
            {this.props.value}
        </button>
        );
    }
}
  
class Board extends React.Component {
    renderSquare(i) {
        return <Square value={i}/>;
    }
  
    render() {
        const status = 'Next player: X';
        return (
            <div>
            <div className="status">{status}</div>
            <div className="board-row">
                {this.renderSquare(0)}
                {this.renderSquare(1)}
                {this.renderSquare(2)}
            </div>
            <div className="board-row">
                {this.renderSquare(3)}
                {this.renderSquare(4)}
                {this.renderSquare(5)}
            </div>
            <div className="board-row">
                {this.renderSquare(6)}
                {this.renderSquare(7)}
                {this.renderSquare(8)}
            </div>
            </div>
        );
    }
}
  
class Game extends React.Component {
    render() {
        return (
            <div className="game">
            <div className="game-board">
                <Board />
            </div>
            <div className="game-info">
                <div>{/* status }</div>
                <ol>{/* TODO }</ol>
            </div>
            </div>
        );
    }
}*/
  
  // ========================================

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

class ListAsset extends React.Component{
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

ReactDOM.render(
    <div>
        <Layout>
            <Header>
                <LineTree />
            </Header>
            <Content>
                <ListAsset header="Lent" data={owned}/>
                <ListAsset header="Assets" data={available}/>
            </Content>
        </Layout>
    </div>,
    document.getElementById('root')
);