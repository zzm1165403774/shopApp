import { useStore } from 'vuex'
import { computed } from 'vue'
export const useCommonCart = (shopId) => {
  const store = useStore()
  const cartList = store.state.cartList
  const change = (shopId, productId, productInfo, x) => {
    store.commit('changeItemToCart', { shopId, productId, productInfo, x })
  }
  const productList = computed(() => {
    const productList = cartList[shopId]?.productList || {}
    const notEmpty = {}
    // eslint-disable-next-line prefer-const
    for (let i in productList) {
      const product = productList[i]
      if (product.count > 0) {
        notEmpty[i] = product
      }
    }
    return notEmpty
  })
  const shopName = computed(() => {
    const shopName = cartList[shopId]?.shopName || ''
    return shopName
  })
  const calculations = computed(() => {
    const productList = cartList[shopId]?.productList
    const result = {
      total: 0,
      price: 0,
      allChecked: true
    }
    if (productList) {
      // eslint-disable-next-line prefer-const
      for (let i in productList) {
        const product = productList[i]
        result.total += product.count
        if (product.check) {
          result.price += (product.count * product.price)
        }
        if (product.count > 0 && !product.check) {
          result.allChecked = false
        }
      }
    }
    result.price = result.price.toFixed(2)
    return result
  })
  return { change, cartList, productList, shopName, calculations }
}
