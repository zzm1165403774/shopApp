<template>
    <div class="products">
        <div class="products__title">{{shopName}}</div>
        <div class="products__list">
            <div
                v-for="item in productList" :key="item._id"
                class="products__item"
            >
                <img class="products__item__img" :src="item.imgUrl">
                <div class="products__item__detail">
                    <h4 class="products__item__title">{{item.name}}</h4>
                    <p class="products__item__price">
                        <span>
                            <span class="products__item__yen">&yen;</span>
                                {{item.price}} x {{item.count}}
                        </span>
                        <span class="products__item__price__total">
                            <span class="products__item__yen">&yen;</span>
                                {{(item.price * item.count).toFixed(2)}}
                        </span>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useCommonCart } from '../../effects/cartEffects'
import { useRoute } from 'vue-router'
export default {
  name: 'Products',
  setup () {
    const route = useRoute()
    const shopId = route.params.id
    const { productList, shopName } = useCommonCart(shopId)
    return { productList, shopName }
  }
}
</script>
<style lang="scss" scoped>
@import '../../style/mixins.scss';
.products{
    margin: .16rem .18rem .55rem .18rem;
    background-color: #fff;
    &__title{
        font-size: .16rem;
        line-height: .22rem;
        padding: .16rem 0 0 .16rem;
    }
    &__item{
        position: relative;
        display: flex;
        padding: .16rem;
        &__img{
            width: .46rem;
            height: .46rem;
            margin-right: .16rem;
        }
        &__detail{
            flex: 1;
        }
        &__title{
            margin: 0;
            line-height: .2rem;
            font-size: .14rem;
            @include ellipsis;
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
</style>
