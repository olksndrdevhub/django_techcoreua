console.log('it`s working')

let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('light')
}else{
    setTheme(theme)
}

let themeSwitcher = document.getElementsByClassName('theme-mode')


for(var i=0; themeSwitcher.length > i; i++){
    themeSwitcher[i].addEventListener('click', function(){
        let mode = this.dataset.mode
        console.log('Option clicked: ', mode)
        setTheme(mode)
    })
}



function setTheme(mode) {
    if(mode == 'dark'){
        document.getElementById('theme-style').href = dark_style_src
    }
    if(mode == 'light'){
        document.getElementById('theme-style').href = def_style_src
    }

    localStorage.setItem('theme', mode)
} 