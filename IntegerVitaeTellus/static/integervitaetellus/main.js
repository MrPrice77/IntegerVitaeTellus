const vm = new Vue ({
    el: '#menu',
    data: {
        title: "",
        image: "",
        recipes: [],
    },
    delimiters: ["[[","]]"],
    methods: {
        getRecipes: function() {
            axios({
                method: 'get',
                url: '/api/v1/',
            }).then(response => {
                this.recipes = response.data
            })
        }
    },
    mounted: function() {
        this.getRecipes()
    }
})