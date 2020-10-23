import gql from 'graphql-tag'

export const videosWithPaginationQuery = gql`
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

export const allGenresQuery = gql`
  query AllGenres($skip: Int, $limit: Int) {
    genres(skip: $skip, limit: $limit) {
      id
      name
    }
  }
`
