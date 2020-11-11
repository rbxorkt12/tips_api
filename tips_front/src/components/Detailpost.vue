<template>
<div class="b-card">
    {{targetpost.rating_average}}
    <br>
    {{targetpost.content}}
</div>
</template>

<script>
export default {
    name: 'PostDetail',
    data: () => {
        return {}
    },
    props: {
        targetpost: {}
    },
    methods: {
        test() {
            () => {
                console.log(this.targetpost)
            }
        }
    }
}
</script>
