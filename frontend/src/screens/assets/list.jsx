import React, { Component } from "react";
import { Typography, List, Avatar } from "antd";
import { Query } from "react-apollo";
import { Link } from "react-router-dom";

import { QUERY_ASSETS } from "./api";

import ContentCard from "../../components/ContentCard";

const { Title } = Typography;

export default class Assets extends Component {
    componentDidMount() { }
    render() {
        return (
            <ContentCard>
                <Title level={3}>Asset Lent</Title>
                <div style={{ maxHeight: 300, overflowY: "scroll" }}>
                    <Query query={QUERY_ASSETS}>
                        {({ loading, error, data }) => {
                            console.log("loading: ", loading);
                            console.log("data: ", data);
                            console.log("error: ", error);
                            return (
                                loading || (
                                    <List
                                        itemLayout="horizontal"
                                        dataSource={data.teams}
                                        renderItem={item => (
                                            <List.Item>
                                                <List.Item.Meta
                                                    avatar={<Avatar src={""} />}
                                                    title={<Link to="/detail">{item.name}</Link>}
                                                    description={item.organization.name}
                                                />
                                                <div>20/03/2017</div>
                                            </List.Item>
                                        )}
                                    />
                                )
                            );
                        }}
                    </Query>
                </div>
            </ContentCard>
        );
    }
}
