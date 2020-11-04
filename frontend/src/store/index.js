import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    state: {
      videos: [],
      video: {}
    },

    getters: {
      getVideos: state => state.videos,
      getVideo: state => state.video
    },

    mutations: {
      updateVideos: (state, videos) => {
        state.videos = videos
      },
      updateVideo: (state, video) => {
        state.video = video
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  })

  return Store
}
