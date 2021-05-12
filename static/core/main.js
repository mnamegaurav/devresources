// Function to search the items
const searchItems = (e) => {
    const searchInput = document.getElementById("id_search_term")
    const searchTerm = searchInput.value

    // Hide the top resources if user is searching
    // if(searchTerm){
    //     document.getElementById('top_resource_categories_cards').classList.add('hidden')
    // } else{
    //     document.getElementById('top_resource_categories_cards').classList.remove('hidden')
    // }
    
    // All the cards
    const allResourceCards = document.querySelectorAll(".resource_category_card")

    // Hide the unmatched results
    allResourceCards.forEach((card)=>{
        if(card.id.includes(searchTerm)){
            card.classList.remove('hidden')
        } else{
            card.classList.add('hidden')
        }
    })

    // hide the whole group if no results matched in that group
    const allResourceGroups = document.querySelectorAll('.resource_category_group')
    allResourceGroups.forEach((group)=>{

        allCardsOfThisGroup = group.querySelectorAll('.resource_category_card')
        allHiddenCardsOfThisGroup = group.querySelectorAll('.resource_category_card.hidden')

        if(allCardsOfThisGroup.length === allHiddenCardsOfThisGroup.length){
            // Hide all the groups and cards
            group.classList.add('hidden')
        } else{
            group.classList.remove('hidden')
        }
    })

    // All the groups which are hidden
    const allHiddeResourceGroups = document.querySelectorAll('.resource_category_group.hidden')
    
    // If all the groups are hidden then show no results text
    if(allResourceGroups.length === allHiddeResourceGroups.length){
        document.getElementById('no_results_text').classList.remove('hidden')
    }else{
        document.getElementById('no_results_text').classList.add('hidden')
    }
}