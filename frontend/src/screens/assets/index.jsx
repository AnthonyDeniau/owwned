import React, { Component } from "react";
import { Typography, List, Avatar } from "antd";
import { Query } from "react-apollo";

import { QUERY_ASSETS } from "./api";

import ClassicLayout from "../../layouts/classic";
import ContentCard from "../../components/ContentCard";

const { Title } = Typography;

export default class AssetsHomeScreen extends Component {
  componentDidMount() {}
  render() {
    return (
      <ClassicLayout breadcrumb={[{ text: "Home" }, { text: "Assets" }]}>
        <ContentCard>
          <Title level={3}>Asset Lent</Title>
          <div style={{ maxHeight: 300, overflowY: "scroll" }}>
            <Query query={QUERY_ASSETS}>
              {({ loading, error, data }) => {
                console.log("loading: ", loading);
                return (
                  loading || (
                    <List
                      itemLayout="horizontal"
                      dataSource={data.pokemons}
                      renderItem={item => (
                        <List.Item>
                          <List.Item.Meta
                            avatar={<Avatar src={item.image} />}
                            title={<a href="https://ant.design">{item.name}</a>}
                            description={item.maxHP + " HP"}
                          />
                          <div>{item.classification}</div>
                        </List.Item>
                      )}
                    />
                  )
                );
              }}
            </Query>
          </div>
        </ContentCard>
      </ClassicLayout>
    );
  }
}
