import { createStore } from 'vuex'
const setLocalStorage = (state) => {
  const { cartList } = state
  const cartListString = JSON.stringify(cartList)
  localStorage.cartList = cartListString
}
const getLocalStorage = () => {
  try {
    return JSON.parse(localStorage.cartList)
  } catch (e) {
    return {}
  }
}
export default createStore({
  state: {
    cartList: getLocalStorage()
    // shopId: {
    //   shopName:'沃尔玛'
    //   productList:{
    //     productId: {
    //     _id: '1',
    //     name: '番茄 250g / 份',
    //     imgUrl: 'http://www.dell-lee.com/imgs/vue3/tomato.png',
    //     sales: 10,
    //     price: 33.6,
    //     oldPrice: 39.6,
    //     count: 2
    //   }
    // }
    // }
  },
  mutations: {
    changeItemToCart (state, payload) {
      const { shopId, productId, productInfo, x } = payload
      // eslint-disable-next-line prefer-const
      let shopInfo = state.cartList[shopId] || {
        shopName: '', productList: {}
      }
      let product = shopInfo.productList[productId]
      if (!product) {
        product = productInfo
        product.count = 0
      }
      product.count = product.count + x
      if (x > 0) { product.check = true }
      if (product.count < 0) product.count = 0
      shopInfo.productList[productId] = product
      state.cartList[shopId] = shopInfo
      setLocalStorage(state)
    },
    changeCheck (state, payload) {
      const { shopId, productId } = payload
      const product = state.cartList[shopId].productList[productId]
      product.check = !product.check
      setLocalStorage(state)
    },
    cleanCart (state, payload) {
      const { shopId } = payload
      state.cartList[shopId].productList = {}
      setLocalStorage(state)
    },
    selectAll (state, payload) {
      const { shopId } = payload
      const products = state.cartList[shopId].productList
      if (products) {
        for (const i in products) {
          const product = products[i]
          product.check = true
        }
      }
      setLocalStorage(state)
    },
    changeShopName (state, payload) {
      const { shopId, shopName } = payload
      const shopInfo = state.cartList[shopId] || {
        shopName: '', productList: {}
      }
      shopInfo.shopName = shopName
      state.cartList[shopId] = shopInfo
      setLocalStorage(state)
    }
  },
  actions: {
  },
  modules: {
  }
})
