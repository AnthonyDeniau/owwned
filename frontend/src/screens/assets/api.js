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
