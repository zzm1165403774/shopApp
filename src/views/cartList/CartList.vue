<template>
  <div class="wrapper">
    <div class="none">---购物车为空---</div>
    <div class="title">我的全部购物车</div>
    <div class="shops">
      <div class="shop" v-for="item in productList" :key="item">
        <div class="shop__title">{{item.shopName}}</div>
        <div class="product">
          <template
          v-for="(item, index) in item.productList"
          :key="index"
          >
              <div class="product__item" v-if='item.count>0'>
                <img class="product__item__img" :src="item.imgUrl">
                <div class="product__item__detail">
                    <h4 class="product__item__title">{{item.name}}</h4>
                    <p class="product__item__price">
                        <span>
                            <span class="product__item__yen">&yen;</span>
                                {{item.price}} x {{item.count}}
                        </span>
                        <span class="product__item__price__total">
                            <span class="product__item__yen">&yen;</span>
                                {{(item.price * item.count).toFixed(2)}}
                        </span>
                    </p>
                </div>
              </div>
          </template>
        </div>
        <!-- <div class="btn">
          <div class="btn__info"></div>
          <div class="btn__submit">去结算</div>
        </div> -->
      </div>
    </div>
  </div>
  <docker :currentIndex ="1" />
</template>

<script>
import { computed } from 'vue'
import Docker from '../../components/docker'
import { useStore } from 'vuex'
export default {
  name: 'CartList',
  components: { Docker },
  setup () {
    const store = useStore()
    const cartList = store.state.cartList
    const productList = computed(() => {
      const newCartList = {}
      // eslint-disable-next-line prefer-const
      for (let shopId in cartList) {
        let total = 0
        const products = cartList[shopId].productList
        // eslint-disable-next-line prefer-const
        for (let productId in products) {
          const product = products[productId]
          total += (product.count || 0)
        }
        if (total > 0) {
          newCartList[shopId] = cartList[shopId]
        }
      }
      return newCartList
    })
    console.log(productList)
    return { productList }
  }
}
</script>

<style lang="scss" scoped>
.wrapper{
  position: absolute;
  left: 0;
  top: 0;
  bottom: .5rem;
  right: 0;
  padding: 0 .18rem ;
  overflow-y: auto;
  background-color: #f8f8f8;
}
.none{
  position: absolute;
  top: .96rem;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
}
.title{
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
  z-index: 2;
  line-height: .44rem;
  background-color: #fff;
  font-size: .16rem;
  text-align: center;
  border-bottom: .01rem solid #F1F1F1;
}
.shops {
  z-index: 1;
  position: relative;
  margin-top: .6rem;
  // top: .6rem;
  // right: .18rem;
  // bottom: .3rem;
  // left: .18rem;
}
.shop {
  background: #fff;
  margin-bottom: .16rem;
  border-radius: .05rem;
  &__title {
    padding: .16rem;
    font-size: .14rem;
  }
}
.product{
    &__item{
        position: relative;
        display: flex;
        padding: .12rem 0;
        margin: 0 .16rem;
        &__detail{
            flex: 1;
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
        }
        &__price{
            display: flex;
            margin: .06rem 0 0 0;
            line-height: .2rem;
            font-size: .14rem;
            color: #e93b3b;
            &__total{
                flex: 1;
                text-align: right;
                color: #000;
            }
        }
        &__yen{
            font-size: .12rem;
        }
    }
}
.btn{
  display: flex;
  &__info{
    flex: 1;
  }
  &__submit{
    line-height: .32rem;
    font-size: .14rem;
    text-align: center;
    border-radius: .02rem;
    background-color: #4fb0f9;
    width: .6rem;
    margin: .1rem;
  }
}
</style>
