import gql from "graphql-tag";

export const QUERY_ASSETS = gql`
  {
    teams {
      id
      name
      organization {
        name
      }
    }
  }
`;

export const QUERY_ASSET_DETAIL = gql`
  {
    asset(id: 1) {
      name
      description
      cost
    }
  }
`;
