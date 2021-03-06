import gql from 'graphql-tag'

// Date - type graphene-python
const addVideoMutation = gql`
  mutation CreateVideo(
    $title: String!, $summary: String, $genres: [String!], $releaseDate: Date!, $runtime: Int!, $url: String!
  ) {
      createVideo(
        title: $title,
        summary: $summary,
        genres: $genres,
        releaseDate: $releaseDate,
        runtime: $runtime,
        url: $url
      ) {
          video {
            id
            title
            summary
            genres {
              name
            }
            releaseDate
            runtime
            url
          }
      }
  }
`
const addGenreMutation = gql`
  mutation CreateGenre($name: String!) {
    createGenre(name: $name) {
      genre {
        name
      }
    }
  }
`
export { addVideoMutation, addGenreMutation }
