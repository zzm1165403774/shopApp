<template>
    <div v-if="showCart && calculations.total>0" class="mask" @click="showChange"></div>
    <div class="cart">
      <div class="product" v-if="showCart && calculations.total>0">
        <div class="product__header">
          <div class="product__header__all">
            <span
             class="product__header__icon iconfont"
             v-html="calculations.allChecked ? '&#xe63a;': '&#xe66c;'"
             @click="() => selectAll(shopId)"
            ></span>
            全选
          </div>
          <div @click="() => cleanCart(shopId)" class="product__header__clear">清空购物车</div>
        </div>
          <div
            class="product__item"
            v-for="(item, index) in productList"
            :key="index"
          >
            <div
            class="product__item__checked iconfont"
            v-html="item.check? '&#xe63a;':'&#xe66c;' "
            @click="() => changeCheck(shopId, item._id)"
            >
            </div>
            <img class="product__item__img" :src="item.imgUrl">
            <div class="product__item__detail">
                <h4 class="product__item__title">{{item.name}}</h4>
                <p class="product__item__price">
                    <span class="product__item__yen">&yen;</span>{{item.price}}
                    <span class="product__item__origin">&yen;{{item.oldPrice}}</span>
                </p>
            </div>
            <div class="product__number">
                <span @click="() => { change(shopId, item._id, item, -1) }" class="product__number__minus">-</span>
                {{item.count || 0}}
                <span
                @click="() => { change(shopId, item._id, item, 1) }"
                class="product__number__add"
                >+</span>
            </div>
          </div>
    </div>
      <div class="check">
        <div class="icon">
          <img @click="showChange" class="icon__img" src="http://www.dell-lee.com/imgs/vue3/basket.png">
          <div class="icon__img__tag">{{calculations.total}}</div>
        </div>
        <div class="info">
          总计:<span class="info__price">&yen; {{calculations.price}}</span>
        </div>
        <div class="btn" v-show="calculations.total>0">
          <router-link :to="{path: `/orderConfirm/${shopId}`}">
          去结算
          </router-link>
        </div>
      </div>
    </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'
import { useCommonCart } from '../../effects/cartEffects'
const useCart = (shopId) => {
  const store = useStore()
  const cartList = store.state.cartList
  const changeCheck = (shopId, productId) => {
    store.commit('changeCheck', {
      shopId, productId
    })
  }
  const cleanCart = (shopId) => {
    store.commit('cleanCart', { shopId })
  }
  const selectAll = (shopId) => {
    store.commit('selectAll', { shopId })
  }
  const { change, productList, calculations } = useCommonCart(shopId)
  return { selectAll, cartList, changeCheck, cleanCart, calculations, change, productList }
}
export default {
  name: 'cart',
  setup () {
    const route = useRoute()
    const shopId = route.params.id

    const showCart = ref(false)
    const showChange = () => {
      showCart.value = !showCart.value
    }
    const { selectAll, changeCheck, cleanCart, calculations, change, productList } = useCart(shopId)
    return { showChange, showCart, selectAll, productList, change, shopId, changeCheck, cleanCart, calculations }
  }
}
</script>

<style lang="scss" scoped>
@import '../../style/mixins.scss';
.mask{
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,.5);
  z-index: 1;
}
.product{
    background: #fff;
    flex: 1;
    overflow-y:scroll;
    &__header{
      display: flex;
      height: .52rem;
      border-bottom: 1px solid #f1f1f1;
      line-height: .52rem;
      font-size: .14rem;
      color: #333333;
      &__icon{
        font-size: .2rem;
        color: #0091ff;
        display: inline-block;
        vertical-align: top;
      }
      &__all{
        width: .64rem;
        margin-left: .18rem;
      }
      &__clear{
        flex: 1;
        text-align: right;
        margin-right: .18rem;
      }
    }
    &__item{
        position: relative;
        display: flex;
        padding: .12rem 0;
        margin: 0 .16rem;
        border-bottom: .01rem solid #f1f1f1;
        &__checked{
          color: #0091ff;
          font-size: .2rem;
          line-height: .5rem;
          margin-right: .18rem;
        }
        &__detail{
            overflow: hidden;
        }
        &__img{
            width: .46rem;
            height: .46rem;
            margin-right: .16rem;
        }
        &__title{
            margin: 0;
            line-height: .2rem;
            font-size: .14rem;
            @include ellipsis;
        }
        &__price{
            margin: .06rem 0 0 0;
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
.cart{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 2;
  background: #fff;
}
.check{
  display: flex;
  line-height: .49rem;
  box-sizing: border-box;
  height: .49rem;
  border: 1px solid #f1f1f1;
}
.icon{
  position: relative;
  width: .84rem;
  &__img{
    display: block;
    margin: .12rem auto;
    width: .28rem;
    height: .26rem;
    &__tag{
      position: absolute;
      right: .15rem;
      top: 0;
      min-width: .2rem;
      height: .2rem;
      line-height: .2rem;
      background-color: #e93b3b;
      border-radius: 50%;
      font-size: .12rem;
      text-align: center;
      color: #fff;
      transform: scale(.7);
  }
  }
}
.info{
  flex: 1;
  color: #333;
  font-size: .12rem;
  &__price{
    color: #e93b3b;
    font-size: .18rem;
  }
}
.btn{
  width: .98rem;
  line-height: .49rem;
  text-align: center;
  background-color: #4fb09f;
  font-size: .14rem;
  a {
    color: #fff;
    text-decoration: none;
  }
}
</style>
