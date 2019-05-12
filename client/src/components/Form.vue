<template>
    <div class="msg-form">
        <form @submit.prevent="formSubmit">
            <div class="form-author-name">
                <input v-model="author" type="text" :disabled="savedAuthor" name="author_name"
                       :class="{'error': $v.author.$error }" placeholder="Enter your name" />
            </div>
            <div class="form-elements">
                <div class="form-msg-area">
                    <textarea :class="{'error': $v.text.$error }" v-model="text"
                              name="message_text"></textarea>
                    <div v-if="$v.text.$error" class="input-error">This field is required!</div>
                </div>
                <div class="form-submit"><input type="submit" name="submit" value="Send"/></div>
            </div>
        </form>
    </div>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required } from 'vuelidate/lib/validators'

    export default {
        name: "Form",
        mixins: [validationMixin],
        data: () => {
            return {
                author: null, text: null, savedAuthor: null
            }
        },
        mounted() {
            this.author = window.localStorage.getItem('authorName');
            this.savedAuthor = this.author;
        },
        methods: {
            formSubmit: function() {
                this.$v.$touch();

                if (this.$v.$invalid) {
                    return false;
                }

                this.saveAuthorName();

                let msg = {
                    date: new Date(),
                    author: this.author,
                    text: this.text
                };

                this.$emit('formSubmit', msg);

                this.text = null;
                this.$v.$reset();
            },
            saveAuthorName: function () {
                if (this.author) {
                    window.localStorage.setItem('authorName', this.author);
                    this.savedAuthor = this.author;
                }
            }
        },
        validations: {
            text: {
                required
            },
            author: {
                required
            }
        }
    }
</script>

<style scoped>
    .msg-form {
        padding: 15px;
        background-color: #EEEDED;
        height: 150px;
        margin-bottom: auto;
        border-top: 1px solid black;
    }

    .form-elements {
        display: flex;
        align-items: center;
    }

    .form-msg-area {
        flex-grow: 1;
    }

    .form-msg-area textarea {
        margin-top: 10px;
        background-color: #FEFEFE;
        border: none;
        min-height: 85px;
        width: 100%;
        font-family: inherit;
    }

    .form-submit input {
        width: 75px;
        height: 50px;
        background-color: #128C7E;
        border: none;
        border-radius: 10px;
        margin-left: 15px;
        color: #fff;
        font-weight: bold;
        font-size: 16px;
    }

    .form-submit input:hover {
        background-color: #075E54;
    }

    .form-author-name input {
        width: 100%;
        border: none;
        height: 30px;
        text-indent: 10px;
    }

    .error {
        outline: 1px solid red;
    }

    .input-error {
        color: red;
        margin-top: 5px;
    }
</style>
