<template>
  <div class="content">
    <div class="category">
        <div
         :class="{'category__item': true, 'category__item--active': currentTab=== item.tab}"
         v-for="item in categories"
         :key="item"
         @click="handleTab(item.tab)"
        >{{item.name}}</div>
    </div>
    <div class="product">
        <div
         class="product__item"
         v-for="(item, index) in list"
         :key="index"
        >
            <img class="product__item__img" :src="item.imgUrl">
            <div class="product__item__detail">
                <h4 class="product__item__title">{{item.name}}</h4>
                <p class="product__item__sales">月售  {{item.sales}}</p>
                <p class="product__item__price">
                    <span class="product__item__yen">&yen;</span>{{item.price}}
                    <span class="product__item__origin">&yen;{{item.oldPrice}}</span>
                </p>
            </div>
            <div class="product__number">
                <span @click="() => { changeCartItem(shopId, item._id, item, -1, shopName) }" class="product__number__minus">-</span>
                {{cartList?.[shopId]?.productList?.[item._id]?.count || 0}}
                <span
                 @click="() => { changeCartItem(shopId, item._id, item, 1, shopName) }"
                 class="product__number__add"
                >+</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref, toRefs, watchEffect } from 'vue'
import { get } from '../../utils/request'
import { useRoute } from 'vue-router'
import { useCommonCart } from '../../effects/cartEffects'
import { useStore } from 'vuex'
const categories = [{
  name: '全部商品',
  tab: 'all'
}, {
  name: '秒杀',
  tab: 'seckill'
}, {
  name: '新鲜水果',
  tab: 'fruit'
}]

const useTab = () => {
  const currentTab = ref(categories[0].tab)
  const handleTab = (tab) => {
    currentTab.value = tab
  }
  return { currentTab, handleTab }
}

const useCurrentList = (currentTab, shopId) => {
  const content = reactive({ list: [] })
  const getData = async (tab) => {
    const result = await get(`/api/shop/${shopId}/products`, { tab: currentTab.value })
    console.log(result)
    if (result?.errno === 0 && result?.data?.length) {
      content.list = result.data
    }
  }
  watchEffect(() => { getData() })
  const { list } = toRefs(content)
  return { list }
}
const Cart = () => {
  const store = useStore()
  const { change, cartList } = useCommonCart()
  const changeShopName = (shopId, shopName) => {
    store.commit('changeShopName', { shopId, shopName })
  }
  const changeCartItem = (shopId, productId, item, num, shopName) => {
    change(shopId, productId, item, num)
    changeShopName(shopId, shopName)
  }
  return { cartList, changeCartItem }
}
export default {
  props: ['shopName'],
  name: 'Content',
  setup () {
    const route = useRoute()
    const shopId = route.params.id
    console.log(shopId)
    const { currentTab, handleTab } = useTab()
    const { list } = useCurrentList(currentTab, shopId)
    const { changeCartItem, cartList } = Cart()
    return { shopId, cartList, currentTab, list, categories, handleTab, changeCartItem }
  }
}
</script>

<style lang="scss" scoped>
@import '../../style/mixins.scss';
.content{
    display: flex;
    position: absolute;
    left: 0;
    right: 0;
    top: 1.5rem;
    bottom: .5rem;
}
.category{
    width: .76rem;
    background: #f5f5f5;
    height: 100%;
    overflow-y:scroll;
    &__item{
        line-height: .4rem;
        text-align: center;
        font-size: .14rem;
        color: #333;
        &--active{
            background: #fff;
        }
    }
}
.product{
    flex: 1;
    overflow-y:scroll;
    &__item{
        position: relative;
        display: flex;
        padding: .12rem 0;
        margin: 0 .16rem;
        border-bottom: .01rem solid #f1f1f1;
        &__detail{
            overflow: hidden;
        }
        &__img{
            width: .68rem;
            height: .68rem;
            margin-right: .16rem;
        }
        &__title{
            margin: 0;
            line-height: .2rem;
            font-size: .14rem;
            @include ellipsis;
        }
        &__sales{
            margin: .06rem 0;
            line-height: .16rem;
            font-size: .13rem;
            color: #333;
        }
        &__price{
            margin: 0;
            line-height: .2rem;
            font-size: .14rem;
            color: #e93b3b;
        }
        &__yen{
            font-size: .12rem;
        }
        &__origin{
            line-height: .2rem;
            font-size: .12rem;
            color: #999;
            text-decoration: line-through;
            margin-left: .04rem;
        }
        .product__number{
            position: absolute;
            right: 0;
            bottom: .12rem;
            &__add,
            &__minus{
                display: inline-block;
                width: .2rem;
                height: .2rem;
                border-radius: 50%;
                font-size: .2rem;
                text-align: center;
                line-height: .16rem;
            }
            &__minus{
                color: #666;
                 border: .01rem solid #666;
                 margin-right: .05rem;
            }
            &__add{
                background: #0091ff;
                margin-left: .05rem;
            }
        }
    }
}
</style>
