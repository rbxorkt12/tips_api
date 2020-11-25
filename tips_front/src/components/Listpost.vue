<template>
<div class="ListTips">
    <button v-on:click="getPosts">Get whole post</button>
    <b-card header="Whole post in such Domain" style="max-width: 40rem; margin: auto; margin-top: 10vh;" class="mb-2" border-variant="info" align="left">
        <b-form-group id="to-do-input">
            <b-container fluid>
                <b-row class="my-1">
                    <b-col sm="10">
                        <b-form-input v-model="title" type="text" placeholder="새 할 일을 적으세요." />
                    </b-col>
                    <b-col sm="2">
                        <b-button variant="outline-primary">추가</b-button>
                    </b-col>
                </b-row>
            </b-container>
        </b-form-group>
        <b-list-group v-if="posts && posts.length">
            <b-list-group-item v-for="post of posts" v-bind:data="post.title" v-bind:key="post.id">
                <b-form-checkbox v-model="post.done">
                    {{post.title}}
                </b-form-checkbox>
                <div class="card-text"> {{post.rating_average}}</div>
                <button class="btn-sm btn-primary mt-2 mb-3" @click="postDetail(post)">Detail</button>
            </b-list-group-item>
        </b-list-group>
    </b-card>
    <Detailpost v-bind:targetpost="targetpost"></Detailpost>
</div>
</template>

<script>
import axios from 'axios'
import Detailpost from './Detailpost'
export default {
    components: {
        Detailpost
    },
    name: 'Listpost',
    data: () => {
        return {
            posts: [],
            targetpost: Object,
            requesturl: 'http://127.0.0.1:8000/api/'
        }
    },

    methods: {
        getPosts() {
            axios.get(this.requesturl + 'post/posts/').then(
                (res) => {
                    this.posts = res.data
                }
            ).catch(err => console.log(err))
        },
        postDetail(post) {
            this.targetpost = post;
            console.log(this.targetpost)
        }

    }
}
</script>
