import React, { Component } from "react";
import { Descriptions, Typography } from "antd";
import { Query } from "react-apollo";

import { QUERY_ASSET_DETAIL } from "./api";

import ContentCard from "../../components/ContentCard";

const { Title } = Typography;

export default class AssetDetailScreen extends Component {
    render() {
        return (
            <ContentCard>
                <Title level={4}>Informations</Title>
                <div>
                    <Query query={QUERY_ASSET_DETAIL}>
                        {({ loading, error, data }) => {
                            return (
                                loading || (
                                    <Descriptions>
                                        <Descriptions.Item label="Name">{data.asset.name}</Descriptions.Item>
                                        <Descriptions.Item label="Description">{data.asset.description}</Descriptions.Item>
                                        <Descriptions.Item label="Cost">{data.asset.cost}</Descriptions.Item>
                                    </Descriptions>
                                )
                            )
                        }}
                    </Query>
                </div>
            </ContentCard>
        );
    }
}