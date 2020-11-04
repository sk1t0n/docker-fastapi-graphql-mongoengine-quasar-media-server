import gql from 'graphql-tag'

const videosWithPaginationQuery = gql`
  query VideosWithPagination($skip: Int, $limit: Int) {
    videos(skip: $skip, limit: $limit) {
      id
      title
      summary
      genres {
        id
        name
      }
      releaseDate
      runtime
      url
    }
  }
`

const videoCountQuery = gql`
  query VideoCount {
    videoCount
  }
`

const videoQuery = gql`
  query Video($id: ID!) {
    video(id: $id) {
      id
      title
      summary
      genres {
        id
        name
      }
      releaseDate
      runtime
      url
    }
  }
`

const allGenresQuery = gql`
  query AllGenres($skip: Int, $limit: Int) {
    genres(skip: $skip, limit: $limit) {
      id
      name
    }
  }
`

export { videosWithPaginationQuery, videoCountQuery, videoQuery, allGenresQuery }
