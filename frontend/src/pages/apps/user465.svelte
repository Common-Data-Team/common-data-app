<script>
    import ProfileInfo from './_components/Profile_Info.svelte';

    let data = {
        user_name: "user",
        user_surname: "Драгун",
        user_avatar_link: "/images/user_images/user465.jpg",
        tags: [
            {
                tag_name: "Здоровье",
                tag_href: "/health"
            },
            {
                tag_name: "Наука",
                tag_href: "/health"
            },
            {
                tag_name: "Наука",
                tag_href: "/health"
            },
            {
                tag_name: "Наука",
                tag_href: "/health"
            }
        ],
        about:'23 y.o. designer from San Francisco',
        projects: [
            {
                title: "Карта ночного неба",
                project_href: "/project325"
            },
            {
                title: "Влияние проходимого расстояния на здоровье",
                project_href: "/project"
            },
            {
                title: "Карта ночного неба",
                project_href: "/project325"
            }
        ]
    }
</script>

<ProfileInfo {...data}></ProfileInfo>