import gql from "graphql-tag";

export const QUERY_ASSETS = gql`
  {
    pokemons(first: 10) {
      name
      maxHP
      classification
      image
    }
  }
`;
